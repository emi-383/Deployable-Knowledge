# Benchmark Suite
This folder contains the benchmarking infrastructure for the pipeline.

## Python
Unlike the core Typescript code, all files in this folder are in **Python** to natively support the **BEIR (Benchmarking Information Retrieval)** framework, which is built on Python ecosystem.

## Setup (only run 1st time)
```bash
npm install
cd py-benchmark 
python -m venv .venv
```
* macOS/Linux:
`source .venv/bin/activate`
* Windows:
`.\.venv\Scripts\activate`

```bash
pip install -r requirements.txt
python data_load.py
cd ..
```

## Run (each time pipeline is changed)
```bash
npm run prep-benchmark
cd py-benchmark
python evaluate.py
cd ..
```

## Switching Datasets
To test the RAG pipeline against different types of retrieval tests, you can easily swap the active dataset.

1. Open `py-benchmark/data_load.py`.

2. Locate the `DATASET_TYPE` constant near the top of the file and change it to one of the supported options:
   * "scifact" - scientific, technical, or fact verification
   * "hotpotqa" - multihop reasoning
   * "nfcorpus" - TREC-Covid: biomedical terminology
   * "nq" - Natural Questions: simulate real user general queries
   
3. Navigate to the benchmark folder and run the loader script again to download the new dataset and sync the TypeScript compiler:

```bash
cd py-benchmark
python data_load.py
cd ..
