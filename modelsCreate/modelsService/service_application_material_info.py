"""
业务办理-申报材料表
"""
import uuid
from sqlalchemy import Column, String, Text, DateTime, CHAR, ForeignKey, func
from sqlalchemy.dialects.mysql import LONGBLOB
from modelsCreate.base import Base

class ServiceApplicationMaterialInfo(Base):
    __tablename__ = 'service_application_material_info'

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

    # 文件类型
    file_type = Column(String(100), nullable=True, comment='文件类型')

    # 材料形式（纸质/电子/原件/复印件）
    material_form = Column(String(50), nullable=True, comment='材料形式')

    # 材料要求（概括性描述）
    material_requirements = Column(String(500), nullable=True, comment='材料要求')

    # 份数
    material_pagenum = Column(String(50), nullable=True, comment='材料要求(份数)')

    # 材料必要性 1必要
    material_necessity = Column(String(2), nullable=True, comment='材料必要性')

    # 来源渠道
    source_channel = Column(String(100), nullable=True, comment='来源渠道')

    # 设立依据
    basis_of_establishment = Column(Text, nullable=True, comment='设立依据')

    # 填报须知
    filling_instructions = Column(Text, nullable=True, comment='填报须知')

    # 附件下载（存储文件二进制或路径 格式文本 示范文本）
    material_formguid = Column(LONGBLOB, nullable=True, comment='附件下载格式文本')
    material_exampleguid = Column(LONGBLOB, nullable=True, comment='附件下载示范文本')

    # 创建时间
    create_date = Column(DateTime, nullable=True, default=func.current_timestamp(), comment='创建日期')

    def __repr__(self):
        return f"<ApplicationMaterialInfo(file_type='{self.file_type}', material_necessity='{self.material_necessity}')>"