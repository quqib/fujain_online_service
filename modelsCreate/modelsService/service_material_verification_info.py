"""
业务处理-申报材料-核查信息
"""
import uuid
from sqlalchemy import Column, CHAR, DateTime, Text, func, ForeignKey, String
from modelsCreate.base import Base


class ServiceMaterialVerificationInfo(Base):
    __tablename__ = 'service_material_verification_info'

    # 主键：使用 CHAR(36) 存储 UUID 字符串
    rowguid = Column(
        CHAR(36),  # 在数据库中存储为 CHAR(36)
        primary_key=True,
        default=lambda: str(uuid.uuid4()),  # 自动生成 UUID 字符串
        nullable=False,
        comment='主键，UUID 自动生成'
    )

    # 外键：关联到 service_application_material_info 表的 material_unid
    basic_info_rowguid = Column(
        CHAR(36),
        ForeignKey('service_application_material_info.material_unid', ondelete='CASCADE'),
        nullable=False,
        comment='关联 service_application_material_info 表的material_unid字段'
    )

    # 本身节点
    problem_unid = Column(String(36), nullable=True, comment='本身节点')

    # 父级节点
    parent_problem_unid = Column(String(36), nullable=True, comment='父级节点')

    # 本身字段
    problem_name = Column(String(2000), nullable=True, comment='本身字段')

    # 创建时间
    create_date = Column(DateTime, nullable=True, default=func.current_timestamp(), comment='创建时间')

    def __repr__(self):
        return f"<StandardizedItemCatalog(item_code='{self.item_code}', item_type='{self.item_type}')>"