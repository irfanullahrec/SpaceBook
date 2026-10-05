import struct, base64, math

file_path = r"C:\Users\Shehroz Khan\Downloads\pdf-jpg-bulk-converter (1).html"

# Generate 1-second 8000Hz 16-bit mono WAV with a 25Hz low-frequency sine wave
sample_rate = 8000
duration = 1.0
num_samples = int(sample_rate * duration)
freq = 25.0
amplitude = 1200 # -28dB, above Chrome's -60dB silence threshold

raw_samples = bytearray()
for i in range(num_samples):
    val = int(amplitude * math.sin(2 * math.pi * freq * i / sample_rate))
    raw_samples.extend(struct.pack('<h', val))

data_size = len(raw_samples)
riff_size = 36 + data_size
header = struct.pack('<4sI4s4sIHHIIHH4sI',
    b'RIFF', riff_size, b'WAVE',
    b'fmt ', 16, 1, 1, sample_rate, sample_rate * 2, 2, 16,
    b'data', data_size
)

wav_b64 = base64.b64encode(header + raw_samples).decode('ascii')
wav_uri = f"data:audio/wav;base64,{wav_b64}"

with open(file_path, "r", encoding="utf-8") as f:
    c = f.read()

# Replace the previous keep-alive section with the bulletproof version
old_keepalive_start = "/* Background Keep-Alive & Anti-Throttling System */"
old_keepalive_end = "function yieldToMain() {"
start_idx = c.find(old_keepalive_start)
end_idx = c.find(old_keepalive_end)
assert start_idx != -1 and end_idx != -1, "Could not find keep-alive block"

# Find end of yieldToMain function
yield_end_idx = c.find("document.querySelectorAll(\".tab\")", end_idx)
assert yield_end_idx != -1, "Could not find yieldToMain end"

new_keepalive_code = f"""/* Background Keep-Alive & Anti-Throttling System */
let keepAliveCtx = null, keepAliveOsc = null, wakeLock = null, backgroundWorker = null, keepAliveAudio = null;

const INAUDIBLE_WAV = "{wav_uri}";

try {{
  const workerBlob = new Blob([
    'let timer = null; self.onmessage = function(e) {{ if (e.data === "start") {{ if (!timer) timer = setInterval(function() {{ self.postMessage("tick"); }}, 30); }} else if (e.data === "stop") {{ clearInterval(timer); timer = null; }} }};'
  ], {{ type: 'application/javascript' }});
  backgroundWorker = new Worker(URL.createObjectURL(workerBlob));
}} catch(e) {{}}

async function startKeepAlive() {{
  // 1. HTML5 Audio element playing looping sub-audible tone
  // Signals Chrome & Windows OS audio engine that tab has active audible media
  // Chrome NEVER suspends or freezes tabs that are playing audible media!
  try {{
    if (!keepAliveAudio) {{
      keepAliveAudio = new Audio(INAUDIBLE_WAV);
      keepAliveAudio.loop = true;
      keepAliveAudio.volume = 0.05;
    }}
    await keepAliveAudio.play().catch(() => {{}});
  }} catch(e) {{}}

  // 2. Web Audio API oscillator (25 Hz sub-audible tone with active gain)
  try {{
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (AudioCtx) {{
      if (!keepAliveCtx) keepAliveCtx = new AudioCtx();
      if (keepAliveCtx.state === 'suspended') await keepAliveCtx.resume();
      if (!keepAliveOsc) {{
        keepAliveOsc = keepAliveCtx.createOscillator();
        keepAliveOsc.type = 'sine';
        keepAliveOsc.frequency.setValueAtTime(25, keepAliveCtx.currentTime);
        const gain = keepAliveCtx.createGain();
        gain.gain.setValueAtTime(0.04, keepAliveCtx.currentTime); // -28 dB: well above Chrome's -60dB silence threshold
        keepAliveOsc.connect(gain);
        gain.connect(keepAliveCtx.destination);
        keepAliveOsc.start();
      }}
    }}
  }} catch(e) {{}}

  // 3. Screen Wake Lock
  try {{
    if ('wakeLock' in navigator && !wakeLock) {{
      wakeLock = await navigator.wakeLock.request('screen').catch(() => {{}});
    }}
  }} catch(e) {{}}

  // 4. Background Web Worker ticker
  try {{
    if (backgroundWorker) backgroundWorker.postMessage('start');
  }} catch(e) {{}}
}}

function stopKeepAlive() {{
  try {{
    if (keepAliveAudio) {{
      keepAliveAudio.pause();
      keepAliveAudio.currentTime = 0;
      keepAliveAudio = null;
    }}
  }} catch(e) {{}}
  try {{ if (backgroundWorker) backgroundWorker.postMessage('stop'); }} catch(e) {{}}
  try {{ if (wakeLock) {{ wakeLock.release().catch(() => {{}}); wakeLock = null; }} }} catch(e) {{}}
  try {{
    if (keepAliveOsc) {{ keepAliveOsc.stop(); keepAliveOsc.disconnect(); keepAliveOsc = null; }}
    if (keepAliveCtx) {{ keepAliveCtx.close().catch(() => {{}}); keepAliveCtx = null; }}
  }} catch(e) {{}}
}}

function dataURLtoBlob(dataUrl) {{
  const parts = dataUrl.split(',');
  const mime = parts[0].match(/:(.*?);/)[1];
  const bstr = atob(parts[1]);
  let n = bstr.length;
  const u8arr = new Uint8Array(n);
  while (n--) {{
    u8arr[n] = bstr.charCodeAt(n);
  }}
  return new Blob([u8arr], {{ type: mime }});
}}

function yieldToMain() {{
  return new Promise(resolve => {{
    if (typeof MessageChannel !== 'undefined') {{
      const mc = new MessageChannel();
      mc.port1.onmessage = () => resolve();
      mc.port2.postMessage(null);
    }} else {{
      setTimeout(resolve, 0);
    }}
  }});
}}

"""

c = c[:start_idx] + new_keepalive_code + c[yield_end_idx:]

# Now replace the convertJpg body with synchronous toDataURL and memory cleanup
old_convert_body = """      const page=await pdf.getPage(i), vp=page.getViewport({scale:sc});
      const canvas=document.createElement("canvas");
      canvas.width=Math.ceil(vp.width);canvas.height=Math.ceil(vp.height);
      await page.render({canvasContext:canvas.getContext("2d",{alpha:false}),viewport:vp}).promise;
      const blob=await new Promise(r=>canvas.toBlob(r,"image/jpeg",q));
      const name=`${pdfFile.name.replace(/\\.pdf$/i,"")}_page_${String(i).padStart(3,"0")}.jpg`;
      const url=URL.createObjectURL(blob);jpgResults.push({blob,name,url});
      const div=document.createElement("div");div.className="item";
      div.innerHTML=`<div class="num">${i}</div><img src="${url}" loading="lazy"><a style="display:block;text-align:center;margin-top:7px;color:#236a58;font-weight:bold" href="${url}" download="${name}">Download JPG</a>`;
      $("jpgGrid").appendChild(div);$("pdfBar").style.width=(i/pdf.numPages*100)+"%";
      await yieldToMain();"""

new_convert_body = """      const page=await pdf.getPage(i), vp=page.getViewport({scale:sc});
      const canvas=document.createElement("canvas");
      canvas.width=Math.ceil(vp.width);canvas.height=Math.ceil(vp.height);
      const ctx=canvas.getContext("2d",{alpha:false});
      await page.render({canvasContext:ctx,viewport:vp,useRequestAnimationFrame:false}).promise;
      const dataUrl=canvas.toDataURL("image/jpeg",q);
      const blob=dataURLtoBlob(dataUrl);
      canvas.width=1;canvas.height=1; // Release canvas GPU/RAM memory immediately
      const name=`${pdfFile.name.replace(/\\.pdf$/i,"")}_page_${String(i).padStart(3,"0")}.jpg`;
      const url=URL.createObjectURL(blob);jpgResults.push({blob,name,url});
      const div=document.createElement("div");div.className="item";
      div.innerHTML=`<div class="num">${i}</div><img src="${url}" loading="lazy"><a style="display:block;text-align:center;margin-top:7px;color:#236a58;font-weight:bold" href="${url}" download="${name}">Download JPG</a>`;
      $("jpgGrid").appendChild(div);$("pdfBar").style.width=(i/pdf.numPages*100)+"%";
      await yieldToMain();"""

assert old_convert_body in c, "Could not find old_convert_body"
c = c.replace(old_convert_body, new_convert_body)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(c)

print("FILE SUCCESSFULLY UPDATED WITH BULLETPROOF KEEP-ALIVE!")
