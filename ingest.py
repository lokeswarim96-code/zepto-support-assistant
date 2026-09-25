from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer

BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "docs"
CHROMA_DIR = BASE_DIR / "chroma_db"

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=str(CHROMA_DIR))

collection = client.get_or_create_collection(
    name="zepto_policies"
)

def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


documents = []
metadatas = []
ids = []

for file_path in sorted(DOCS_DIR.glob("*.txt")):
    text = file_path.read_text(encoding="utf-8")
    chunks = chunk_text(text)

    for index, chunk in enumerate(chunks):
        documents.append(chunk)
        metadatas.append({
            "source": file_path.name
        })
        ids.append(f"{file_path.stem}_{index}")


embeddings = model.encode(
    documents,
    normalize_embeddings=True
).tolist()

if documents:
    collection.upsert(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings
    )

print(f"Documents processed: {len(list(DOCS_DIR.glob('*.txt')))}")
print(f"Chunks stored: {len(documents)}")
print("ChromaDB collection:", collection.name)
print("Embedding model: all-MiniLM-L6-v2")
print("Ingestion completed successfully.")