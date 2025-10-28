# 导入基本配置
from config.seetings import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelsCreate.base import Base


# 创建引擎和会话
engine = create_engine(DATABASE_URL, echo=False)  # echo=True 可查看 SQL 输出
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """创建表（如果不存在）"""
    Base.metadata.create_all(bind=engine)
    print("✅ 表创建完成（如果不存在）")
