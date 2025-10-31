"""
业务办理-常见问题
"""
import uuid
from sqlalchemy import Column, CHAR, DateTime, Text, func, ForeignKey
from modelsCreate.base import Base


class ServiceAskedQuestionInfo(Base):
    __tablename__ = 'service_asked_question_info'

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

    # 问题名称
    question_name = Column(Text, nullable=True, index=True, comment='问题名称')

    # 问题内容
    question_content = Column(Text, nullable=True, index=True, comment='问题内容')

    # 创建时间
    create_date = Column(DateTime, nullable=True, default=func.current_timestamp(), comment='创建时间')

    def __repr__(self):
        return f"<StandardizedItemCatalog(item_code='{self.item_code}', item_type='{self.item_type}')>"

