"""
特殊环节表
"""
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SpecialProceduresInfo(Base):
    __tablename__ = 'special_procedures_info'

    # 主键
    rowguid = Column(String(50), primary_key=True, nullable=False, comment='主键')

    # 特殊环节名称
    special_link_name = Column(String(200), nullable=True, comment='特殊环节名称')
    # 示例：听证、招标、拍卖、检验、检测、检疫、鉴定、专家评审等

    # 承诺时限（单位：工作日）
    commitment_limit = Column(String(50), nullable=True, comment='承诺时限')
    # 可存储为 "10个工作日" 或仅数字 "10"

    # 设立依据
    basis_of_establishment = Column(String(2000), nullable=True, comment='设立依据')
    # 法律、法规或政策依据，如《行政许可法》第四十五条

    # 审计字段（建议通用字段）
    create_date = Column(String(10), nullable=True, comment='创建日期')  # 格式：YYYY-MM-DD
    # update_date = Column(String(10), nullable=True, comment='更新时间')  # 格式：YYYY-MM-DD
    # state = Column(String(1), nullable=True, comment='状态')  # '1'=有效，'0'=无效

    def __repr__(self):
        return f"<SpecialProceduresInfo(special_link_name='{self.special_link_name}', commitment_limit='{self.commitment_limit}')>"