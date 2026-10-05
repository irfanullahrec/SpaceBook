import re

file_path = r"C:\Users\Shehroz Khan\Downloads\pdf-jpg-bulk-converter (1).html"

with open(file_path, "r", encoding="utf-8") as f:
    c = f.read()

# 1. Insert Background Keep-Alive & Anti-Throttling System
helpers = """let pdfDownloadUrls=[];

/* Background Keep-Alive & Anti-Throttling System */
let keepAliveCtx = null, keepAliveOsc = null, wakeLock = null, backgroundWorker = null;

try {
  const workerBlob = new Blob([
    'let timer = null; self.onmessage = function(e) { if (e.data === "start") { if (!timer) timer = setInterval(function() { self.postMessage("tick"); }, 40); } else if (e.data === "stop") { clearInterval(timer); timer = null; } };'
  ], { type: 'application/javascript' });
  backgroundWorker = new Worker(URL.createObjectURL(workerBlob));
} catch(e) {}

async function startKeepAlive() {
  try {
    if ('wakeLock' in navigator && !wakeLock) {
      wakeLock = await navigator.wakeLock.request('screen');
    }
  } catch(e) {}
  try {
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (AudioCtx) {
      if (!keepAliveCtx) keepAliveCtx = new AudioCtx();
      if (keepAliveCtx.state === 'suspended') await keepAliveCtx.resume();
      if (!keepAliveOsc) {
        keepAliveOsc = keepAliveCtx.createOscillator();
        const gain = keepAliveCtx.createGain();
        gain.gain.value = 0.00001; // completely inaudible, signals Chrome that tab is active media so it never freezes
        keepAliveOsc.connect(gain);
        gain.connect(keepAliveCtx.destination);
        keepAliveOsc.start();
      }
    }
  } catch(e) {}
  try {
    if (backgroundWorker) backgroundWorker.postMessage('start');
  } catch(e) {}
}

function stopKeepAlive() {
  try { if (backgroundWorker) backgroundWorker.postMessage('stop'); } catch(e) {}
  try { if (wakeLock) { wakeLock.release().catch(()=>{}); wakeLock = null; } } catch(e) {}
  try {
    if (keepAliveOsc) { keepAliveOsc.stop(); keepAliveOsc.disconnect(); keepAliveOsc = null; }
    if (keepAliveCtx) { keepAliveCtx.close().catch(()=>{}); keepAliveCtx = null; }
  } catch(e) {}
}

function yieldToMain() {
  return new Promise(resolve => {
    if (typeof MessageChannel !== 'undefined') {
      const mc = new MessageChannel();
      mc.port1.onmessage = () => resolve();
      mc.port2.postMessage(null);
    } else {
      setTimeout(resolve, 0);
    }
  });
}
"""

c = c.replace("let pdfDownloadUrls=[];", helpers)

# 2. Update convertJpg handler
old_convert = """$("convertJpg").onclick=async()=>{
  if(!pdfFile)return;
  $("convertJpg").disabled=true;$("zipJpg").disabled=true;
  $("jpgGrid").innerHTML="";jpgResults=[];
  try{
    $("pdfStatus").textContent="Loading PDF...";
    const pdf=await pdfjsLib.getDocument({data:await pdfFile.arrayBuffer()}).promise;
    const q=Math.max(.1,Math.min(1,Number($("jpgQuality").value)||.92));
    const sc=Math.max(1,Math.min(4,Number($("jpgScale").value)||1.5));
    for(let i=1;i<=pdf.numPages;i++){
      $("pdfStatus").textContent=`Converting page ${i} of ${pdf.numPages}...`;
      const page=await pdf.getPage(i), vp=page.getViewport({scale:sc});
      const canvas=document.createElement("canvas");
      canvas.width=Math.ceil(vp.width);canvas.height=Math.ceil(vp.height);
      await page.render({canvasContext:canvas.getContext("2d",{alpha:false}),viewport:vp}).promise;
      const blob=await new Promise(r=>canvas.toBlob(r,"image/jpeg",q));
      const name=`${pdfFile.name.replace(/\\.pdf$/i,"")}_page_${String(i).padStart(3,"0")}.jpg`;
      const url=URL.createObjectURL(blob);jpgResults.push({blob,name,url});
      const div=document.createElement("div");div.className="item";
      div.innerHTML=`<div class="num">${i}</div><img src="${url}" loading="lazy"><a style="display:block;text-align:center;margin-top:7px;color:#236a58;font-weight:bold" href="${url}" download="${name}">Download JPG</a>`;
      $("jpgGrid").appendChild(div);$("pdfBar").style.width=(i/pdf.numPages*100)+"%";
      await new Promise(r=>setTimeout(r,0));
    }
    $("pdfStatus").textContent=`Done — ${pdf.numPages} page(s) converted.`;
    $("zipJpg").disabled=false;
  }catch(e){console.error(e);$("pdfStatus").textContent="Error: "+e.message}
  $("convertJpg").disabled=false;
};"""

new_convert = """$("convertJpg").onclick=async()=>{
  if(!pdfFile)return;
  $("convertJpg").disabled=true;$("zipJpg").disabled=true;
  $("jpgGrid").innerHTML="";jpgResults=[];
  await startKeepAlive();
  try{
    $("pdfStatus").textContent="Loading PDF...";
    const pdf=await pdfjsLib.getDocument({data:await pdfFile.arrayBuffer()}).promise;
    const q=Math.max(.1,Math.min(1,Number($("jpgQuality").value)||.92));
    const sc=Math.max(1,Math.min(4,Number($("jpgScale").value)||1.5));
    for(let i=1;i<=pdf.numPages;i++){
      $("pdfStatus").textContent=`Converting page ${i} of ${pdf.numPages}...`;
      document.title = `(${i}/${pdf.numPages}) Converting... - Bulk PDF Converter`;
      const page=await pdf.getPage(i), vp=page.getViewport({scale:sc});
      const canvas=document.createElement("canvas");
      canvas.width=Math.ceil(vp.width);canvas.height=Math.ceil(vp.height);
      await page.render({canvasContext:canvas.getContext("2d",{alpha:false}),viewport:vp}).promise;
      const blob=await new Promise(r=>canvas.toBlob(r,"image/jpeg",q));
      const name=`${pdfFile.name.replace(/\\.pdf$/i,"")}_page_${String(i).padStart(3,"0")}.jpg`;
      const url=URL.createObjectURL(blob);jpgResults.push({blob,name,url});
      const div=document.createElement("div");div.className="item";
      div.innerHTML=`<div class="num">${i}</div><img src="${url}" loading="lazy"><a style="display:block;text-align:center;margin-top:7px;color:#236a58;font-weight:bold" href="${url}" download="${name}">Download JPG</a>`;
      $("jpgGrid").appendChild(div);$("pdfBar").style.width=(i/pdf.numPages*100)+"%";
      await yieldToMain();
    }
    $("pdfStatus").textContent=`Done — ${pdf.numPages} page(s) converted.`;
    document.title = `Done (${pdf.numPages} pages) - Bulk PDF Converter`;
    $("zipJpg").disabled=false;
  }catch(e){
    console.error(e);
    $("pdfStatus").textContent="Error: "+e.message;
    document.title = "Error - Bulk PDF Converter";
  }finally{
    stopKeepAlive();
    $("convertJpg").disabled=false;
  }
};"""

if old_convert in c:
    c = c.replace(old_convert, new_convert)
    print("convertJpg replaced successfully")
else:
    print("WARNING: old_convert not found")

# 3. Update makePdf handler
old_makepdf_top = """$("makePdf").onclick=async()=>{
  if(!imageFiles.length)return;
  clearPdfDownloads();
  $("makePdf").disabled=true;
  try{"""

new_makepdf_top = """$("makePdf").onclick=async()=>{
  if(!imageFiles.length)return;
  clearPdfDownloads();
  $("makePdf").disabled=true;
  await startKeepAlive();
  try{"""

if old_makepdf_top in c:
    c = c.replace(old_makepdf_top, new_makepdf_top)
    print("makePdf top replaced")

old_yield1 = 'records.push({jpeg:compressed.jpeg,width:compressed.width,height:compressed.height,pageW,pageH,x,y,w,h,sourcePage:i+1});\n      $("imgBar").style.width=((i+1)/imageFiles.length*100)+"%";\n      await new Promise(r=>setTimeout(r,0));'
new_yield1 = 'records.push({jpeg:compressed.jpeg,width:compressed.width,height:compressed.height,pageW,pageH,x,y,w,h,sourcePage:i+1});\n      $("imgBar").style.width=((i+1)/imageFiles.length*100)+"%";\n      document.title = `(${i+1}/${imageFiles.length}) Compressing... - Bulk PDF Converter`;\n      await yieldToMain();'
if old_yield1 in c:
    c = c.replace(old_yield1, new_yield1)
    print("yield 1 replaced")

old_yield2 = 'outputs.push({blob:pdf,name:baseName+suffix+".pdf",pages:groups[i]});\n      await new Promise(r=>setTimeout(r,0));'
new_yield2 = 'outputs.push({blob:pdf,name:baseName+suffix+".pdf",pages:groups[i]});\n      document.title = `(${i+1}/${groups.length}) Building PDF... - Bulk PDF Converter`;\n      await yieldToMain();'
if old_yield2 in c:
    c = c.replace(old_yield2, new_yield2)
    print("yield 2 replaced")

old_makepdf_bot = """  }catch(e){console.error(e);$("imgStatus").textContent="Error: "+e.message}
  $("makePdf").disabled=false;
};"""

new_makepdf_bot = """    document.title = "Done - Bulk PDF Converter";
  }catch(e){
    console.error(e);
    $("imgStatus").textContent="Error: "+e.message;
    document.title = "Error - Bulk PDF Converter";
  }finally{
    stopKeepAlive();
    $("makePdf").disabled=false;
  }
};"""
if old_makepdf_bot in c:
    c = c.replace(old_makepdf_bot, new_makepdf_bot)
    print("makePdf bottom replaced")

# 4. Update makeWord handler
old_makeword_top = """$("makeWord").onclick=async()=>{
  if(!wordImageFiles.length)return;
  $("makeWord").disabled=true;
  try{"""

new_makeword_top = """$("makeWord").onclick=async()=>{
  if(!wordImageFiles.length)return;
  $("makeWord").disabled=true;
  await startKeepAlive();
  try{"""
if old_makeword_top in c:
    c = c.replace(old_makeword_top, new_makeword_top)
    print("makeWord top replaced")

old_yield3 = '$("wordBar").style.width=((i+1)/wordImageFiles.length*100)+"%";\n      await new Promise(resolve=>setTimeout(resolve,0));'
new_yield3 = '$("wordBar").style.width=((i+1)/wordImageFiles.length*100)+"%";\n      document.title = `(${i+1}/${wordImageFiles.length}) Preparing Word... - Bulk PDF Converter`;\n      await yieldToMain();'
if old_yield3 in c:
    c = c.replace(old_yield3, new_yield3)
    print("yield 3 replaced")

old_makeword_bot = """  }catch(e){console.error(e);$("wordStatus").textContent="Error: "+e.message}
  $("makeWord").disabled=false;
};"""

new_makeword_bot = """    document.title = "Done - Bulk PDF Converter";
  }catch(e){
    console.error(e);
    $("wordStatus").textContent="Error: "+e.message;
    document.title = "Error - Bulk PDF Converter";
  }finally{
    stopKeepAlive();
    $("makeWord").disabled=false;
  }
};"""
if old_makeword_bot in c:
    c = c.replace(old_makeword_bot, new_makeword_bot)
    print("makeWord bottom replaced")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(c)

print("FILE SAVED SUCCESSFULLY")
