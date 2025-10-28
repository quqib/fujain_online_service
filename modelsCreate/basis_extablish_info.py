"""
设立依据表
"""
import uuid
from sqlalchemy import Column, String, DateTime, Text, ForeignKey, CHAR, func
from .base import Base

class BasisEstablishInfo(Base):
    __tablename__ = 'basis_establish_info'

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

    # 依据文件名称
    basis_file_name = Column(String(500), nullable=True, comment='依据文件名称')
    # 示例：《中华人民共和国行政许可法》

    # 依据文号
    basis_doc_number = Column(String(200), nullable=True, comment='依据文号')
    # 示例：主席令第7号、国发〔2020〕1号

    # 颁布机关
    issuing_authority = Column(String(200), nullable=True, comment='颁布机关')
    # 示例：全国人民代表大会、国务院、住房和城乡建设部

    # 实施日期
    effective_date = Column(String(100), nullable=True, comment='实施日期')
    # 使用 Date 类型，便于日期计算和查询

    # 依据级别（可枚举）
    basis_level = Column(String(50), nullable=True, comment='依据级别')
    # 建议值：'法律', '行政法规', '部门规章', '地方性法规', '规范性文件', '国家标准' 等

    # 条款内容（长文本）
    clause_content = Column(Text, nullable=True, comment='条款内容')
    # 存储具体法律条文内容，支持大段文本

    # 审计字段（建议）
    create_date = Column(DateTime, nullable=True, default=func.current_timestamp(), comment='创建日期')
    # update_date = Column(Date, nullable=True, comment='更新时间')
    # state = Column(String(1), nullable=True, comment='状态')  # '1'=有效，'0'=无效

    def __repr__(self):
        return f"<BasisEstablishInfo(basis_file_name='{self.basis_file_name}', basis_doc_number='{self.basis_doc_number}')>"
