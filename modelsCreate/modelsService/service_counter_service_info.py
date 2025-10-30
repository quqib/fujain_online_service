"""
业务办理-窗口办理信息表
"""
import uuid
from sqlalchemy import Column, String, Text, CHAR, DateTime, func, ForeignKey
from modelsCreate.base import Base


class ServiceCounterServiceInfo(Base):
    __tablename__ = 'service_counter_service_info'

    # 主键：使用 CHAR(36) 存储 UUID 字符串
    rowguid = Column(
        CHAR(36),  # 在数据库中存储为 CHAR(36)
        primary_key=True,
        default=lambda: str(uuid.uuid4()),  # 自动生成 UUID 字符串
        nullable=False,
        comment='主键，UUID 自动生成'
    )

    # 外键：关联到 service_basic_information_info 表的 rowguid
    basic_info_rowguid = Column(
        CHAR(36),
        ForeignKey('service_basic_information_info.rowguid', ondelete='CASCADE'),
        nullable=False,
        comment='关联 service_basic_information_info 表的主键'
    )

    # 办理时间（如“周一至周五 9:00-12:00”）
    handling_time = Column(String(500), nullable=True, comment='办理时间')

    # 办理地点（详细地址）
    service_location = Column(String(500), nullable=True, comment='办理地点')

    # 交通指引（可包含公交、地铁、导航提示等）
    transportation_guide = Column(Text, nullable=True, comment='交通指引')

    # 受理条件
    acceptance_criteria = Column(Text, nullable=True, index=True, comment='受理条件')

    # 创建时间
    create_date = Column(DateTime, nullable=True, default=func.current_timestamp(), comment='创建时间')

    def __repr__(self):
        return f"<WindowServiceInfo(item_code='{self.item_code}', service_location='{self.service_location}')>"