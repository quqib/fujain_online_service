from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ItemQxqInfo(Base):
    __tablename__ = 'item_qxq_info'

    # 主键（建议数据库中设置 PRIMARY KEY）
    rowguid = Column(String(50), primary_key=True, nullable=True, comment='主键')

    # 问题基本信息
    elementname = Column(String(50), nullable=True, comment='问题')                  # 问题简要名称，如：是否首次申请
    elementquestion = Column(String(500), nullable=True, comment='提问文字描述')      # 完整提问语句，用于前端展示
    elementnote = Column(String(500), nullable=True, comment='问题说明')              # 后台说明或补充信息

    # 关联信息
    itemid = Column(String(50), nullable=True, comment='事项版本唯一标识')            # 关联 item_main_info.rowguid（版本ID）
    taskguid = Column(String(50), nullable=True, comment='事项唯一标识')             # 关联 item_main_info.task_guid（事项全局ID）
    elementid = Column(String(50), nullable=True, comment='问题版本唯一标识')         # 问题的版本标识，可用于更新追踪
    preoptionguid = Column(String(50), nullable=True, comment='关联选项标识')         # 用于联动逻辑，指向 item_qxs_info.optionguid 或 catalog_qxs_info
    wikiGuid = Column(String(50), nullable=True, comment='关联法律法规标识')         # 关联 law_info.rowguid
    tagguid = Column(String(50), nullable=True, comment='标签标识')                 # 分类标签，便于管理

    # 控制属性
    multiselect = Column(String(10), nullable=True, comment='是否多选')              # '1'=是, '0'=否；或 'true'/'false'

    # 排序
    ordernum = Column(Integer, nullable=True, comment='排序号')                     # 前端展示顺序

    def __repr__(self):
        return f"<ItemQxqInfo(elementname={self.elementname}, elementquestion='{self.elementquestion[:30]}...')>"