from sqlalchemy import Column, String, Integer, Date, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CatalogQxsInfo(Base):
    __tablename__ = 'catalog_qxs_info'

    # 主键（建议数据库中设置 PRIMARY KEY）
    rowguid = Column(String(50), primary_key=True, nullable=True, comment='主键')

    # 选项基本信息
    optionname = Column(String(50), nullable=True, comment='选项名称')             # 如：是、否、有限责任公司
    optionnote = Column(String(500), nullable=True, comment='备注')               # 后台说明或补充信息

    # 关联信息
    catalogid = Column(String(50), nullable=True, comment='事项版本唯一标识')       # 关联 item_main_info.qaid
    elementguid = Column(String(50), nullable=True, comment='问题标识')            # 关联 catalog_qxq_info.rowguid
    wikiGuid = Column(String(50), nullable=True, comment='关联法律法规标识')       # 关联 law_info.rowguid

    # 材料关联（关键字段）
    materialids = Column(LargeBinary, nullable=True, comment='关联材料标识')        # BLOB 存储：多个材料 rowguid 的 JSON 或逗号分隔字符串
    materialnames = Column(LargeBinary, nullable=True, comment='关联材料名称')      # BLOB 存储：对应材料名称列表

    # 匹配规则（用于复杂场景）
    labeljson = Column(String(1000), nullable=True, comment='选项匹配标签条件')     # JSON 字符串，用于规则引擎匹配，如 {"area": "high-tech", "type": "new"}

    # 排序与状态
    ordernum = Column(Integer, nullable=True, comment='排序号')                   # 前端展示顺序
    state = Column(String(1), nullable=True, comment='状态')                       # '1'=有效, '0'=无效
    create_date = Column(Date, nullable=True, comment='创建时间')
    update_date = Column(Date, nullable=True, comment='更新时间')

    def __repr__(self):
        return f"<CatalogQxsInfo(optionname={self.optionname}, elementguid={self.elementguid})>"