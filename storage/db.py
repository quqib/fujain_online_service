# 导入基本配置
from config.seetings import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelsCreate.base import Base


# 创建引擎和会话
engine = create_engine(DATABASE_URL, echo=True)  # echo=True 可查看 SQL 输出
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """创建表（如果不存在）"""
    Base.metadata.create_all(bind=engine)
    print("✅ 表创建完成（如果不存在）")

# import base64
# import zlib
# from modelsCreate.modelsService.service_application_material_info import ServiceApplicationMaterialInfo

# session = SessionLocal()
#
# # 查询 rowguid = 'C340...' 的记录
# instance = session.get(ServiceApplicationMaterialInfo, '0099231b-9608-4050-90bd-9a1d16489e74')
#
# if instance:
#     # 读取某个字段
#     base64_str = instance.material_formguid  # Base64 字符串
#
#     print(f"文件名: {base64_str}")
#     print(f"类型: {base64_str}")
#     # print(f"内容: {base64_str[:100]}...")  # 打印前100字符
# else:
#     print("未找到该记录")
#
#
# if instance:
#     # 2. 获取字段
#     base64_str = instance.material_formguid
#
#     if not base64_str:
#         print("❌ approval_result_sample 字段为空")
#     else:
#         try:
#             # Step 1: Base64 解码 → 得到压缩后的 bytes
#             compressed_data = base64.b64decode(base64_str)
#
#             # Step 2: zlib 解压缩 → 得到原始文件 bytes
#             original_data = zlib.decompress(compressed_data)
#
#             # 5. 保存到当前目录
#             with open("lalala.pdf", 'wb') as f:
#                 f.write(original_data)
#
#             print(f"✅ 文件已成功下载并保存为：./{"lalala"}")
#             print(f"    大小：{len(original_data)} 字节")
#
#         except Exception as e:
#             print(f"❌ 文件保存失败：{e}")
#
# else:
#     print("❌ 未找到该记录")

