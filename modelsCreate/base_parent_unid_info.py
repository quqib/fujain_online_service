
"""
对照关系表
"""
import uuid
from sqlalchemy import Column, String, DateTime, CHAR, func
from .base import Base

class BaseParentUnidInfo(Base):
    __tablename__ = 'base_parent_unid_info'

    # 主键：使用 CHAR(36) 存储 UUID 字符串
    rowguid = Column(
        CHAR(36),  # 在数据库中存储为 CHAR(36)
        primary_key=True,
        default=lambda: str(uuid.uuid4()),  # 自动生成 UUID 字符串
        nullable=False,
        comment='主键，UUID 自动生成'
    )
    # 父级节点
    parent_unid = Column(String(255), nullable=True, comment='父级节点')
    # 当前节点
    unid = Column(String(255), nullable=True, comment='当前节点')
    # 部门名称
    dept_name = Column(String(2000), nullable=True, comment='部门名称')
    # 词条名称
    commitment_limit = Column(String(2000), nullable=True, comment='词条名称')

    # 审计字段
    create_date = Column(DateTime, nullable=True, default=func.current_timestamp(), comment='创建日期')
    # update_date = Column(Date, nullable=True, comment='更新时间')
    # state = Column(String(1), nullable=True, comment='状态')  # 状态：如 '1'=有效，'0'=无效

    def __repr__(self):
        return f"<ApplicationMaterialInfo(item_code='{self.item_code}', item_type='{self.item_type}')>"


