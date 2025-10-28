import uuid
from sqlalchemy import Column, String, DateTime, CHAR, ForeignKey, func
from sqlalchemy.dialects.mysql import LONGBLOB
from .base import Base

class BasicInformationPictureInfo(Base):
    __tablename__ = 'basic_information_picture_info'

    # 主键：使用 CHAR(36) 存储 UUID 字符串
    rowguid = Column(
        CHAR(36),  # 在数据库中存储为 CHAR(36)
        primary_key=True,
        default=lambda: str(uuid.uuid4()),  # 自动生成 UUID 字符串
        nullable=False,
        comment='主键，UUID 自动生成'
    )

    # 外键：关联到 basic_information_info 表的 rowguid
    basic_info_rowguid = Column(
        CHAR(36),
        ForeignKey('basic_information_info.rowguid', ondelete='CASCADE'),
        nullable=False,
        comment='关联 basic_information_info 表的主键'
    )

    # 文件名称
    approval_result_material_name = Column(String(2000), nullable=True, comment='文件名称')  # 存储为 BLOB

    # 文件内容 二进制存储 图片 docx pdf
    approval_result_material = Column(LONGBLOB, nullable=True, comment='文件内容')

    # 创建时间
    create_date = Column(DateTime, nullable=True, default=func.current_timestamp(), comment='创建日期')