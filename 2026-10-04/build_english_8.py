# build_english_8.py - Generator for Class 8 English (KPTBB)
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# We will construct all 8 units of Class 8 English with:
# - Full textbook verbatim text & paragraphs
# - Line-by-line / paragraph Urdu and Pashto translations
# - Word glossaries with parts of speech, English definition, Urdu & Pashto meanings, sentences
# - Complete textbook exercises (Comprehension Short & Long Questions, MCQs)
# - Grammar lessons & exercises
# - SLO Questions Bank (MCQs, SQs, LQs)
# - English & Urdu chapter summaries

print("Starting generation of Class 8 English dataset...")
