"""
业务办理-基本信息-特殊环节
"""
import uuid
from sqlalchemy import Column, String,CHAR, Text, DateTime, func, ForeignKey
from ..base import Base


class ServiceBasicSpecialSegmentInfo(Base):
    __tablename__ = 'service_basic_special_segment_info'

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

    # 特殊环节名称
    section_name = Column(String(2000), nullable=True, comment='特殊环节名称')

    # 特殊环节时限
    section_time_limit = Column(String(50), nullable=True, comment='特殊环节时限')

    # 特殊环节依据
    Section_basis = Column(Text, nullable=True, comment='特殊环节依据')

    # 特殊环节备注
    Section_remark = Column(Text, nullable=True, comment='特殊环节备注')

    # 创建时间
    create_date = Column(DateTime, nullable=True, default=func.current_timestamp(), comment='创建时间')

    def __repr__(self):
        return f"<NegativeListInfo(item_code='{self.item_code}', item_name='{self.item_name}', measure_code='{self.measure_code}')>"