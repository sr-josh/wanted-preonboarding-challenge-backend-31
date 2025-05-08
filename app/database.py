from sqlalchemy import create_engine, text

# 데이터베이스 엔진  생성
DB_URL = "postgresql://root:root@db:5432/wanted"
engine = create_engine(DB_URL, echo=True)
try:
    connection = engine.connect()
    print("DB 연결 성공")
except Exception as e:
    print("DB 연결 실패:", e)