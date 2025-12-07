#!/usr/bin/env bash
# src/kaggle_download.sh
set -e
# Pastikan kamu sudah menaruh kaggle.json di ~/.kaggle/kaggle.json
mkdir -p ../data/raw
kaggle competitions download -c nlp-getting-started -p ../data/raw
unzip -o ../data/raw/nlp-getting-started.zip -d ../data/raw