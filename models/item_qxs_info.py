from sqlalchemy import Column, String, Integer, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ItemQxsInfo(Base):
    __tablename__ = 'item_qxs_info'

    # 主键（建议数据库中设置 PRIMARY KEY）
    rowguid = Column(String(50), primary_key=True, nullable=True, comment='主键')

    # 选项基本信息
    optionname = Column(String(50), nullable=True, comment='选项名称')               # 如：是、否、有限责任公司
    optionnote = Column(String(500), nullable=True, comment='备注')                 # 后台说明或补充信息

    # 关联信息
    itemid = Column(String(50), nullable=True, comment='事项版本唯一标识')           # 关联 item_main_info.rowguid（版本ID）
    taskguid = Column(String(50), nullable=True, comment='事项唯一标识')            # 关联 item_main_info.task_guid（全局ID）
    optionid = Column(String(50), nullable=True, comment='选项版本唯一标识')         # 用于版本追踪
    elementguid = Column(String(50), nullable=True, comment='问题标识')             # 关联 item_qxq_info.rowguid
    wikiGuid = Column(String(50), nullable=True, comment='关联法律法规标识')        # 关联 law_info.rowguid

    # 材料关联（核心字段）
    materialids = Column(LargeBinary, nullable=True, comment='关联材料标识')          # BLOB 存储：多个材料 rowguid 的 JSON 字符串（bytes）
    materialnames = Column(LargeBinary, nullable=True, comment='关联材料名称')        # BLOB 存储：对应材料名称列表（bytes）

    # 排序与扩展规则
    ordernum = Column(Integer, nullable=True, comment='排序号')                     # 前端展示顺序
    labeljson = Column(String(1000), nullable=True, comment='选项匹配标签条件')      # JSON 字符串，用于复杂规则匹配，如 {"area": "high-tech", "type": "new"})

    def __repr__(self):
        return f"<ItemQxsInfo(optionname={self.optionname}, elementguid={self.elementguid})>"