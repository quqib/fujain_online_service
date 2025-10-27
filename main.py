# main.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
import json

# 导入模型和配置
from models.catalog_info import Base, CatalogInfo
from config.seetings import DATABASE_URL

# 创建引擎和会话
engine = create_engine(DATABASE_URL, echo=True)  # echo=True 可查看 SQL 输出
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """创建表（如果不存在）"""
    Base.metadata.create_all(bind=engine)
    print("✅ 表 catalog_info 创建完成（如果不存在）")

def insert_test_data():
    """插入一条测试数据"""
    db = SessionLocal()
    try:
        test_data = CatalogInfo(
            rowguid="guid_001",
            task_name="企业注册",
            task_type="行政许可",
            by_law=bytes("《公司法》第6条", "utf-8"),  # BLOB 字段传 bytes
            use_level="省级",
            task_state="1",
            task_version=1,
            task_code="S123456789",
            effectplan=date(2025, 1, 1),
            cancelplan=None,
            sjyw_master="市场监管局",
            catalog_type="企业服务",
            is_country_catelog="1",
            is_soncatalog="0",
            areacode="350000",
            law_file=b"file_law_001.pdf",
            remark=bytes("测试备注内容", "utf-8"),
            catalog_id="cat_v001",
            parentid=None,
            version_date=date(2025, 1, 1),
            businesscodes="QY,ZC",
            ordernum=1,
            add_basis=bytes("增补依据说明", "utf-8"),
            user_level_nat_c="国家统一事项",
            user_level_pro_c="福建特色",
            use_level_city_c="市级可办",
            use_level_county_c=bytes("县级需授权", "utf-8"),
            ql_class_name="企业开办",
            if_audit_transer="0",
            audit_transfer_type=None,
            g_fw_content=bytes("提供企业注册一站式服务", "utf-8"),
            g_fw_mode="1",
            g_fw_range="企业服务",
            theme_type="企业开办",
            trade_type="工商",
            is_yw_catalog="1",
            fgf_sign="1",
            create_date=date(2025, 1, 1),
            state="1",
            update_date=date(2025, 1, 1)
        )
        db.add(test_data)
        db.commit()
        print("✅ 测试数据插入成功！")
    except Exception as e:
        db.rollback()
        print(f"❌ 插入失败：{e}")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
    insert_test_data()