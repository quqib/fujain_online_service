"""
基本信息表
"""
from sqlalchemy import Column, String, DateTime, Text, func
from .base import Base

class BasicInformationInfo(Base):
    __tablename__ = 'basic_information_info'

    # 主键
    rowguid = Column(String(50), primary_key=True, nullable=False, comment='主键')

    # 事项基本信息
    item_type = Column(String(100), nullable=True, comment='事项类型')
    exercise_level = Column(String(50), nullable=True, comment='行使层级')
    legal_limit = Column(String(50), nullable=True, comment='法定时限')
    commitment_limit = Column(String(50), nullable=True, comment='承诺时限')
    department_name = Column(String(200), nullable=True, comment='部门名称')
    item_code = Column(String(50), nullable=True, index=True, comment='事项编码')

    # 办理条件
    handling_conditions = Column(Text, nullable=True, comment='办理条件')
    handling_basis = Column(Text, nullable=True, comment='办理条件设立依据')

    # 收费信息
    is_charging = Column(String(2), nullable=True, comment='是否收费')  # 建议：'1'=是，'0'=否

    # 收费类型
    charge_items = Column(String(2000), nullable=True, comment='收费类型')

    # 项目名称
    dir_name = Column(String(200), nullable=True, comment='项目名称')

    # 项目链接
    dir_link = Column(String(2000), nullable=True, comment='项目链接')

    # 审计字段
    create_date = Column(DateTime, nullable=True, default=func.current_timestamp(), comment='创建日期')
    # update_date = Column(Date, nullable=True, comment='更新时间')
    # state = Column(String(1), nullable=True, comment='状态')  # 状态：如 '1'=有效，'0'=无效

    def __repr__(self):
        return f"<ApplicationMaterialInfo(item_code='{self.item_code}', item_type='{self.item_type}')>"