# 导入基本配置
from config.seetings import DATABASE_URL

# 创建引擎和会话
engine = create_engine(DATABASE_URL, echo=True)  # echo=True 可查看 SQL 输出
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
