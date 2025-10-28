"""
特殊环节表
"""
import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime, Text, func
from sqlalchemy.dialects.postgresql import CHAR
from .base import Base

class SpecialProceduresInfo(Base):
    __tablename__ = 'special_procedures_info'

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

    # 特殊环节名称
    special_link_name = Column(String(200), nullable=True, comment='特殊环节名称')
    # 示例：听证、招标、拍卖、检验、检测、检疫、鉴定、专家评审等

    # 承诺时限（单位：工作日）
    commitment_limit = Column(String(50), nullable=True, comment='承诺时限')
    # 可存储为 "10个工作日" 或仅数字 "10"

    # 设立依据
    basis_of_establishment = Column(Text, nullable=True, comment='设立依据')
    # 法律、法规或政策依据，如《行政许可法》第四十五条

    # 审计字段（建议通用字段）
    create_date = Column(DateTime, nullable=True, default=func.current_timestamp(), comment='创建日期')
    # update_date = Column(String(10), nullable=True, comment='更新时间')  # 格式：YYYY-MM-DD
    # state = Column(String(1), nullable=True, comment='状态')  # '1'=有效，'0'=无效

    def __repr__(self):
        return f"<SpecialProceduresInfo(special_link_name='{self.special_link_name}', commitment_limit='{self.commitment_limit}')>"