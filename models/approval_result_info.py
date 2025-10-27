from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ApprovalResultInfo(Base):
    __tablename__ = 'approval_result_info'

    # 主键（建议数据库中设置 PRIMARY KEY）
    rowguid = Column(String(50), primary_key=True, nullable=True, comment='主键')

    # 审批结果基本信息
    result_name = Column(String(200), nullable=True, comment='结果名称')           # 如：营业执照、施工许可证
    result_type = Column(String(30), nullable=True, comment='结果类型')            # 如：证照、批文、备案回执等

    # 证照明细信息（可能用于关联电子证照系统）
    zjmx_name = Column(String(30), nullable=True, comment='证照明细-名称')
    zjmxid = Column(String(100), nullable=True, comment='证照明细-ID')
    zjmx_code = Column(String(50), nullable=True, comment='证照明细-编码')

    # 结果形式与材料关联
    result_dec = Column(String(30), nullable=True, comment='审批结果形式')         # 如：纸质、电子、电子+纸质
    material_code = Column(String(50), nullable=True, comment='材料编码')          # 关联材料目录中的编码

    # 电子证照信息
    is_result_cert = Column(String(2), nullable=True, comment='是否电子证照')       # '1'=是, '0'=否
    cert_code = Column(String(50), nullable=True, comment='电子证照编码')
    cert_name = Column(String(50), nullable=True, comment='电子证照名称')

    # 样本与结果属性
    result_guid = Column(String(500), nullable=True, comment='结果样本')           # 样本文件路径或 GUID（如 PDF 预览链接）
    is_result = Column(String(2), nullable=True, comment='是否有结果')             # '1'=有, '0'=无（如告知性备案）
    is_open = Column(String(2), nullable=True, comment='是否需要面向社会公示')     # '1'=是, '0'=否
    open_area = Column(String(500), nullable=True, comment='公示范围')             # 如：全国、全省、市内

    # 排序与控制字段
    ordernum = Column(Integer, nullable=True, comment='排序号')                   # 前端展示顺序

    # 时间与状态
    create_date = Column(Date, nullable=True, comment='创建日期')
    state = Column(String(1), nullable=True, comment='状态')                       # '1'=有效, '0'=无效
    update_date = Column(Date, nullable=True, comment='更新时间')

    def __repr__(self):
        return f"<ApprovalResultInfo(result_name={self.result_name}, result_type={self.result_type})>"