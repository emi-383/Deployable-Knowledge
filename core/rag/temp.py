'''
testing
python -m core.rag.temp
'''

from core.sessions import KnowledgeBaseStore
from core.database import engine
from core.database.models import BM25ChunkRecord
from sqlmodel import Session, select
kb = KnowledgeBaseStore()
try:
    rec = kb.create_chunk(file_name='x.pdf', text='hi :D', page=1, file_type='text')
    print('created id', rec.id, 'text', rec.text)
except Exception as e:
    print('create error', type(e).__name__, e)
with Session(engine) as s:
    rows = s.exec(select(BM25ChunkRecord)).all()
    print('count', len(rows))
    for r in rows[-3:]:
        print(r.id, r.file_name, r.text[:20])