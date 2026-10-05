import re

path = r'D:\SpaceBook\SpaceBook Web\js\app.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update openSubject in app.js
old_open_subject = """  if (subj.hasBio || subjId === 'cls9-bio' || subjId === 'cls10-bio') {
    state.activeSubject = "bio";
    openSubjectWorkspace(classId, "bio", subj);
  } else if (subj.hasChem || subjId === 'cls9-chem' || subjId === 'cls10-chem' || subjId === 'cls12-chem') {
    state.activeSubject = "chem";
    openSubjectWorkspace(classId, "chem", subj);
  } else if (subj.hasPhys || subjId === 'cls9-phy' || subjId === 'cls10-phy' || subjId === 'cls12-phy') {
    state.activeSubject = "phys";
    openSubjectWorkspace(classId, "phys", subj);
  } else if (subj.hasEng || subjId === 'cls9-eng' || subjId === 'cls10-eng' || subjId === 'cls1-eng' || subjId === 'cls2-eng' || subjId === 'cls3-eng') {
    state.activeSubject = "eng";
    openSubjectWorkspace(classId, "eng", subj);
  } else if (subj.hasUrdu || subjId === 'cls9-urdu' || subjId === 'cls10-urdu' || subjId === 'cls2-urdu') {
    state.activeSubject = "urdu";
    openSubjectWorkspace(classId, "urdu", subj);
  } else if (subj.hasMath || subjId === 'cls1-math' || subjId === 'cls2-math' || subjId === 'cls3-math' || subjId === 'cls9-math' || subjId === 'cls10-math' || subjId === 'cls12-math') {
    state.activeSubject = "math";
    openMathView(classId, subj);
  } else if (subj.hasPakStudy || subjId === 'cls9-pakstudy' || subjId === 'cls10-pakstudy') {
    state.activeSubject = "pakstudy";
    openSubjectWorkspace(classId, "pakstudy", subj);
  } else if (subj.hasNazira || subjId === 'cls1-nazira' || subjId === 'cls2-nazira' || subjId === 'cls3-nazira') {
    state.activeSubject = "nazira";
    openSubjectWorkspace(classId, "nazira", subj);
  } else if (subj.hasPashto || subjId === 'cls1-pashto' || subjId === 'cls2-pashto' || subjId === 'cls3-pashto') {
    state.activeSubject = "pashto";
    openSubjectWorkspace(classId, "pashto", subj);
  } else if (subj.hasIsl || subjId === 'cls9-isl' || subjId === 'cls10-isl' || subjId === 'cls1-isl' || subjId === 'cls2-isl' || subjId === 'cls3-isl') {
    state.activeSubject = "isl";
    openSubjectWorkspace(classId, "isl", subj);
  } else if (subj.hasGk || subjId === 'cls2-gk' || subjId === 'cls1-gk' || subjId === 'cls3-gk') {
    state.activeSubject = "gk";
    openSubjectWorkspace(classId, "gk", subj);
  } else if (subj.hasComp || subjId === 'cls9-comp' || subjId === 'cls10-comp') {
    state.activeSubject = "comp";
    openSubjectWorkspace(classId, "comp", subj);
  } else if (subjId === 'cls12-stat') {
    state.activeSubject = "stat";
    openSubjectWorkspace(classId, "stat", subj);
  } else {"""

new_open_subject = """  if (subj.hasBio || subjId === 'cls9-bio' || subjId === 'cls10-bio' || subjId === 'cls12-bio') {
    state.activeSubject = "bio";
    openSubjectWorkspace(classId, "bio", subj);
  } else if (subj.hasChem || subjId === 'cls9-chem' || subjId === 'cls10-chem' || subjId === 'cls12-chem') {
    state.activeSubject = "chem";
    openSubjectWorkspace(classId, "chem", subj);
  } else if (subj.hasPhys || subjId === 'cls9-phy' || subjId === 'cls10-phy' || subjId === 'cls12-phy') {
    state.activeSubject = "phys";
    openSubjectWorkspace(classId, "phys", subj);
  } else if (subj.hasEng || subjId === 'cls9-eng' || subjId === 'cls10-eng' || subjId === 'cls1-eng' || subjId === 'cls2-eng' || subjId === 'cls3-eng' || subjId === 'cls12-eng') {
    state.activeSubject = "eng";
    openSubjectWorkspace(classId, "eng", subj);
  } else if (subj.hasUrdu || subjId === 'cls9-urdu' || subjId === 'cls10-urdu' || subjId === 'cls2-urdu' || subjId === 'cls12-urdu') {
    state.activeSubject = "urdu";
    openSubjectWorkspace(classId, "urdu", subj);
  } else if (subj.hasMath || subjId === 'cls1-math' || subjId === 'cls2-math' || subjId === 'cls3-math' || subjId === 'cls9-math' || subjId === 'cls10-math' || subjId === 'cls12-math') {
    state.activeSubject = "math";
    openMathView(classId, subj);
  } else if (subj.hasPakStudy || subjId === 'cls9-pakstudy' || subjId === 'cls10-pakstudy' || subjId === 'cls12-pak' || subjId === 'cls12-pakstudy') {
    state.activeSubject = "pakstudy";
    openSubjectWorkspace(classId, "pakstudy", subj);
  } else if (subj.hasNazira || subjId === 'cls1-nazira' || subjId === 'cls2-nazira' || subjId === 'cls3-nazira') {
    state.activeSubject = "nazira";
    openSubjectWorkspace(classId, "nazira", subj);
  } else if (subj.hasPashto || subjId === 'cls1-pashto' || subjId === 'cls2-pashto' || subjId === 'cls3-pashto') {
    state.activeSubject = "pashto";
    openSubjectWorkspace(classId, "pashto", subj);
  } else if (subj.hasIsl || subjId === 'cls9-isl' || subjId === 'cls10-isl' || subjId === 'cls1-isl' || subjId === 'cls2-isl' || subjId === 'cls3-isl') {
    state.activeSubject = "isl";
    openSubjectWorkspace(classId, "isl", subj);
  } else if (subj.hasGk || subjId === 'cls2-gk' || subjId === 'cls1-gk' || subjId === 'cls3-gk') {
    state.activeSubject = "gk";
    openSubjectWorkspace(classId, "gk", subj);
  } else if (subj.hasComp || subjId === 'cls9-comp' || subjId === 'cls10-comp' || subjId === 'cls12-comp') {
    state.activeSubject = "comp";
    openSubjectWorkspace(classId, "comp", subj);
  } else if (subjId === 'cls12-stat') {
    state.activeSubject = "stat";
    openSubjectWorkspace(classId, "stat", subj);
  } else if (subj.hasCivics || subjId === 'cls12-civics') {
    state.activeSubject = "civics";
    openSubjectWorkspace(classId, "civics", subj);
  } else if (subj.hasEcon || subjId === 'cls12-econ') {
    state.activeSubject = "econ";
    openSubjectWorkspace(classId, "econ", subj);
  } else if (subj.hasHpe || subjId === 'cls12-hpe') {
    state.activeSubject = "hpe";
    openSubjectWorkspace(classId, "hpe", subj);
  } else if (subj.hasIslopt || subjId === 'cls12-islopt') {
    state.activeSubject = "islopt";
    openSubjectWorkspace(classId, "islopt", subj);
  } else if (subj.hasIslhist || subjId === 'cls12-islhist') {
    state.activeSubject = "islhist";
    openSubjectWorkspace(classId, "islhist", subj);
  } else if (subj.hasQuran || subjId === 'cls12-quran') {
    state.activeSubject = "quran";
    openSubjectWorkspace(classId, "quran", subj);
  } else {"""

content_norm = content.replace('\r\n', '\n')
if old_open_subject in content_norm:
    content_norm = content_norm.replace(old_open_subject, new_open_subject)
    print("Updated openSubject in app.js")
else:
    print("WARNING: old_open_subject not found!")

# 2. Update SUBJECT_THEMES in app.js
old_themes_tail = """  gk: {
    gradient: 'linear-gradient(135deg, #065f46 0%, #047857 100%)',
    pillBg: '#6ee7b7',
    pillColor: '#022c22',
    accentColor: '#059669',
    tag: 'سبق'
  }
};"""

new_themes_tail = """  gk: {
    gradient: 'linear-gradient(135deg, #065f46 0%, #047857 100%)',
    pillBg: '#6ee7b7',
    pillColor: '#022c22',
    accentColor: '#059669',
    tag: 'سبق'
  },
  stat: {
    gradient: 'linear-gradient(135deg, #4c1d95 0%, #6d28d9 100%)',
    pillBg: '#c4b5fd',
    pillColor: '#2e1065',
    accentColor: '#7c3aed',
    tag: 'Unit'
  },
  civics: {
    gradient: 'linear-gradient(135deg, #1e293b 0%, #334155 100%)',
    pillBg: '#cbd5e1',
    pillColor: '#0f172a',
    accentColor: '#475569',
    tag: 'باب'
  },
  econ: {
    gradient: 'linear-gradient(135deg, #065f46 0%, #047857 100%)',
    pillBg: '#a7f3d0',
    pillColor: '#064e3b',
    accentColor: '#059669',
    tag: 'باب'
  },
  hpe: {
    gradient: 'linear-gradient(135deg, #9a3412 0%, #c2410c 100%)',
    pillBg: '#fed7aa',
    pillColor: '#7c2d12',
    accentColor: '#ea580c',
    tag: 'باب'
  },
  islopt: {
    gradient: 'linear-gradient(135deg, #14532d 0%, #166534 100%)',
    pillBg: '#bbf7d0',
    pillColor: '#052e16',
    accentColor: '#15803d',
    tag: 'باب'
  },
  islhist: {
    gradient: 'linear-gradient(135deg, #78350f 0%, #92400e 100%)',
    pillBg: '#fde68a',
    pillColor: '#451a03',
    accentColor: '#b45309',
    tag: 'باب'
  },
  quran: {
    gradient: 'linear-gradient(135deg, #064e3b 0%, #065f46 100%)',
    pillBg: '#6ee7b7',
    pillColor: '#022c22',
    accentColor: '#059669',
    tag: 'باب'
  }
};"""

if old_themes_tail in content_norm:
    content_norm = content_norm.replace(old_themes_tail, new_themes_tail)
    print("Updated SUBJECT_THEMES in app.js")
else:
    print("WARNING: old_themes_tail not found!")

# 3. Update getSubjectChapterList in app.js
old_ch_list_pattern = r"function getSubjectChapterList\(subjKey, classId\) \{[\s\S]*?return \[\];\s*\}"

new_ch_list = """function getSubjectChapterList(subjKey, classId) {
  if (subjKey === 'math') return getMathChapterList(classId);
  if (subjKey === 'eng') {
    const isCls12 = (classId === 'cls12' || state.selectedClass === 'cls12');
    if (isCls12 && typeof ENGLISH_12_DATA !== 'undefined' && Array.isArray(ENGLISH_12_DATA)) {
      return ENGLISH_12_DATA;
    }
    const isCls10 = (classId === 'cls10' || state.selectedClass === 'cls10');
    if (isCls10 && typeof ENGLISH_10_DATA !== 'undefined' && Array.isArray(ENGLISH_10_DATA)) {
      return ENGLISH_10_DATA;
    }
    const isCls3 = (classId === 'cls3' || state.selectedClass === 'cls3');
    if (isCls3 && typeof ENGLISH_3_DATA !== 'undefined' && Array.isArray(ENGLISH_3_DATA)) {
      return ENGLISH_3_DATA;
    }
    const isCls2 = (classId === 'cls2' || state.selectedClass === 'cls2');
    if (isCls2 && typeof ENGLISH_2_DATA !== 'undefined' && Array.isArray(ENGLISH_2_DATA)) {
      return ENGLISH_2_DATA;
    }
    const isCls1 = (classId === 'cls1' || state.selectedClass === 'cls1');
    if (isCls1 && typeof ENGLISH_1_DATA !== 'undefined' && Array.isArray(ENGLISH_1_DATA)) {
      return ENGLISH_1_DATA;
    }
    return (typeof ENGLISH_DATA !== 'undefined' && Array.isArray(ENGLISH_DATA))
      ? ENGLISH_DATA
      : ((typeof DATA !== "undefined" && DATA && (DATA.englishChapters || DATA.engChapters)) ? (DATA.englishChapters || DATA.engChapters) : []);
  }
  if (subjKey === 'urdu') {
    const isCls12 = (classId === 'cls12' || state.selectedClass === 'cls12');
    if (isCls12 && typeof URDU_12_DATA !== 'undefined' && Array.isArray(URDU_12_DATA)) {
      return URDU_12_DATA;
    }
    const isCls10 = (classId === 'cls10' || state.selectedClass === 'cls10');
    if (isCls10 && typeof URDU_10_DATA !== 'undefined' && Array.isArray(URDU_10_DATA)) {
      return URDU_10_DATA;
    }
    const isCls2 = (classId === 'cls2' || state.selectedClass === 'cls2');
    if (isCls2 && typeof URDU_2_DATA !== 'undefined' && Array.isArray(URDU_2_DATA)) {
      return URDU_2_DATA;
    }
    return (typeof URDU_DATA !== 'undefined' && Array.isArray(URDU_DATA))
      ? URDU_DATA
      : ((typeof DATA !== "undefined" && DATA && (DATA.urduChapters || DATA.urduLessons)) ? (DATA.urduChapters || DATA.urduLessons) : []);
  }
  if (subjKey === 'phys') {
    if (classId === 'cls12' && typeof PHYS_12_DATA !== 'undefined') return PHYS_12_DATA;
    const isCls10 = (classId === 'cls10' || state.selectedClass === 'cls10');
    if (isCls10 && DATA && DATA.phys10Chapters) return DATA.phys10Chapters;
    return (DATA && DATA.physChapters) ? DATA.physChapters : [];
  }
  if (subjKey === 'chem') {
    if (classId === 'cls12' && typeof CHEM_12_DATA !== 'undefined') return CHEM_12_DATA;
    const isCls10 = (classId === 'cls10' || state.selectedClass === 'cls10');
    if (isCls10 && DATA && DATA.chem10Chapters) return DATA.chem10Chapters;
    return (DATA && DATA.chemChapters) ? DATA.chemChapters : [];
  }
  if (subjKey === 'stat' && classId === 'cls12' && typeof STAT_12_DATA !== 'undefined') return STAT_12_DATA;
  if (subjKey === 'bio') {
    const isCls12 = (classId === 'cls12' || state.selectedClass === 'cls12');
    if (isCls12 && typeof BIOLOGY_12_DATA !== 'undefined' && Array.isArray(BIOLOGY_12_DATA)) {
      return BIOLOGY_12_DATA;
    }
    const isCls10 = (classId === 'cls10' || state.selectedClass === 'cls10');
    if (isCls10 && DATA && DATA.bio10Chapters) return DATA.bio10Chapters;
    return (typeof BIO_DATA !== 'undefined' && Array.isArray(BIO_DATA))
      ? BIO_DATA
      : ((typeof DATA !== "undefined" && DATA && (DATA.bioChapters || DATA.bio10Chapters)) ? (DATA.bioChapters || DATA.bio10Chapters) : []);
  }
  if (subjKey === 'pakstudy') {
    const isCls12 = (classId === 'cls12' || state.selectedClass === 'cls12');
    if (isCls12 && typeof PAKSTUDY_12_DATA !== 'undefined' && Array.isArray(PAKSTUDY_12_DATA)) {
      return PAKSTUDY_12_DATA;
    }
    const isCls10 = (classId === 'cls10' || state.selectedClass === 'cls10');
    if (isCls10 && typeof PAKSTUDY_10_DATA !== 'undefined' && Array.isArray(PAKSTUDY_10_DATA)) {
      return PAKSTUDY_10_DATA;
    }
    return (typeof PAKSTUDY_DATA !== 'undefined' && Array.isArray(PAKSTUDY_DATA))
      ? PAKSTUDY_DATA
      : ((typeof DATA !== "undefined" && DATA && DATA.pakstudyChapters) ? DATA.pakstudyChapters : []);
  }
  if (subjKey === 'isl') {
    const isCls10 = (classId === 'cls10');
    if (isCls10 && typeof ISLAMYAT_10_DATA !== 'undefined' && Array.isArray(ISLAMYAT_10_DATA)) {
      return ISLAMYAT_10_DATA;
    }
    const isCls3 = (classId === 'cls3' || state.selectedClass === 'cls3');
    if (isCls3 && typeof ISLAMYAT_3_DATA !== 'undefined' && Array.isArray(ISLAMYAT_3_DATA)) {
      return ISLAMYAT_3_DATA;
    }
    const isCls2 = (classId === 'cls2' || state.selectedClass === 'cls2');
    if (isCls2 && typeof ISLAMYAT_2_DATA !== 'undefined' && Array.isArray(ISLAMYAT_2_DATA)) {
      return ISLAMYAT_2_DATA;
    }
    const isCls1 = (classId === 'cls1');
    if (isCls1 && typeof ISLAMYAT_1_DATA !== 'undefined' && Array.isArray(ISLAMYAT_1_DATA)) {
      return ISLAMYAT_1_DATA;
    }
    return (typeof ISLAMYAT_DATA !== 'undefined' && Array.isArray(ISLAMYAT_DATA))
      ? ISLAMYAT_DATA
      : ((typeof DATA !== "undefined" && DATA && (DATA.islChapters || DATA.islData)) ? (DATA.islChapters || DATA.islData) : []);
  }
  if (subjKey === 'nazira') {
    const isCls3 = (classId === 'cls3' || state.selectedClass === 'cls3');
    if (isCls3 && typeof NAZIRA_3_DATA !== 'undefined' && Array.isArray(NAZIRA_3_DATA)) {
      return NAZIRA_3_DATA;
    }
    const isCls2 = (classId === 'cls2' || state.selectedClass === 'cls2');
    if (isCls2 && typeof NAZIRA_2_DATA !== 'undefined' && Array.isArray(NAZIRA_2_DATA)) {
      return NAZIRA_2_DATA;
    }
    if (typeof NAZIRA_1_DATA !== 'undefined' && Array.isArray(NAZIRA_1_DATA)) {
      return NAZIRA_1_DATA;
    }
    return (typeof DATA !== 'undefined' && DATA && DATA.nazira1Chapters) ? DATA.nazira1Chapters : [];
  }
  if (subjKey === 'pashto') {
    const isCls3 = (classId === 'cls3' || state.selectedClass === 'cls3');
    if (isCls3 && typeof PASHTO_3_DATA !== 'undefined' && Array.isArray(PASHTO_3_DATA)) {
      return PASHTO_3_DATA;
    }
    const isCls2 = (classId === 'cls2' || state.selectedClass === 'cls2');
    if (isCls2 && typeof PASHTO_2_DATA !== 'undefined' && Array.isArray(PASHTO_2_DATA)) {
      return PASHTO_2_DATA;
    }
    if (typeof PASHTO_1_DATA !== 'undefined' && Array.isArray(PASHTO_1_DATA)) {
      return PASHTO_1_DATA;
    }
    return (typeof DATA !== 'undefined' && DATA && DATA.pashto1Chapters) ? DATA.pashto1Chapters : [];
  }
  if (subjKey === 'gk') {
    const isCls3 = (classId === 'cls3' || state.selectedClass === 'cls3');
    if (isCls3 && typeof GK_3_DATA !== 'undefined' && Array.isArray(GK_3_DATA)) {
      return GK_3_DATA;
    }
    const isCls2 = (classId === 'cls2' || state.selectedClass === 'cls2');
    if (isCls2 && typeof GK_2_DATA !== 'undefined' && Array.isArray(GK_2_DATA)) {
      return GK_2_DATA;
    }
    return (typeof DATA !== 'undefined' && DATA && DATA.gk2Chapters) ? DATA.gk2Chapters : [];
  }
  if (subjKey === 'comp') {
    const isCls12 = (classId === 'cls12' || state.selectedClass === 'cls12');
    if (isCls12 && typeof COMP_12_DATA !== 'undefined' && Array.isArray(COMP_12_DATA)) {
      return COMP_12_DATA;
    }
    return (typeof DATA !== 'undefined' && DATA && DATA.compChapters) ? DATA.compChapters : [];
  }
  if (subjKey === 'civics') {
    if (typeof CIVICS_12_DATA !== 'undefined') return CIVICS_12_DATA;
    return (typeof DATA !== 'undefined' && DATA && DATA.civics12Chapters) ? DATA.civics12Chapters : [];
  }
  if (subjKey === 'econ') {
    if (typeof ECON_12_DATA !== 'undefined') return ECON_12_DATA;
    return (typeof DATA !== 'undefined' && DATA && DATA.econ12Chapters) ? DATA.econ12Chapters : [];
  }
  if (subjKey === 'hpe') {
    if (typeof HPE_12_DATA !== 'undefined') return HPE_12_DATA;
    return (typeof DATA !== 'undefined' && DATA && DATA.hpe12Chapters) ? DATA.hpe12Chapters : [];
  }
  if (subjKey === 'islopt') {
    if (typeof ISLAMIAT_OPT_12_DATA !== 'undefined') return ISLAMIAT_OPT_12_DATA;
    return (typeof DATA !== 'undefined' && DATA && DATA.islamiatOpt12Chapters) ? DATA.islamiatOpt12Chapters : [];
  }
  if (subjKey === 'islhist') {
    if (typeof ISLAMIC_HISTORY_12_DATA !== 'undefined') return ISLAMIC_HISTORY_12_DATA;
    return (typeof DATA !== 'undefined' && DATA && DATA.islHist12Chapters) ? DATA.islHist12Chapters : [];
  }
  if (subjKey === 'quran') {
    if (typeof QURAN_12_DATA !== 'undefined') return QURAN_12_DATA;
    return (typeof DATA !== 'undefined' && DATA && DATA.quran12Chapters) ? DATA.quran12Chapters : [];
  }
  return [];
}"""

if re.search(old_ch_list_pattern, content_norm):
    content_norm = re.sub(old_ch_list_pattern, new_ch_list, content_norm)
    print("Updated getSubjectChapterList in app.js")
else:
    print("WARNING: old_ch_list_pattern not found!")

# 4. Update selectSubjectChapter in app.js
old_select_subj = """  const subs = DATA.subjects[classId] || [];
  const subjObj = subs.find(s => s.id === state.activeSubject || s.id === 'cls12-stat' || s.hasEng || s.hasUrdu || s.hasBio || s.hasChem || s.hasPhys || s.hasPakStudy || s.hasIsl || s.hasNazira || s.hasPashto || s.hasStat);"""

new_select_subj = """  const subs = DATA.subjects[classId] || [];
  const subjObj = subs.find(s => s.id === state.activeSubject || s.id === 'cls12-' + subjKey || (subjKey === 'pakstudy' && (s.id === 'cls12-pak' || s.id === 'cls12-pakstudy')) || (subjKey === 'phys' && s.id === 'cls12-phy') || s.hasEng || s.hasUrdu || s.hasBio || s.hasChem || s.hasPhys || s.hasPakStudy || s.hasIsl || s.hasNazira || s.hasPashto || s.hasStat || s.hasComp || s.hasCivics || s.hasEcon || s.hasHpe || s.hasIslopt || s.hasIslhist || s.hasQuran);"""

if old_select_subj in content_norm:
    content_norm = content_norm.replace(old_select_subj, new_select_subj)
    print("Updated selectSubjectChapter in app.js")
else:
    print("WARNING: old_select_subj not found!")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content_norm)
print("Saved app.js")
