// Text fix on scan 207 Pashto (duplicated verb in the first paragraph of Platyhelminthes).
(function () {
  const ch = BIO_11_DATA.find(c => c.id === 'bio11-diversity-animals');
  const sec = ch.sections.find(s => s.id === 'bio11-s207-obelia-corals-bilateria-platyhelminthes');
  const p = sec.paras.find(x => x.id === 'bio11-s207-p4');
  p.pashto = p.pashto.replace('بلل کېږي بلل کېږي', 'بلل کېږي');
})();
