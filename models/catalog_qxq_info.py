from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CatalogQxqInfo(Base):
    __tablename__ = 'catalog_qxq_info'

    # 主键（建议数据库中设置 PRIMARY KEY）
    rowguid = Column(String(50), primary_key=True, nullable=True, comment='主键')

    # 问题基本信息
    elementname = Column(String(100), nullable=True, comment='问题名称')           # 如：企业类型、是否首次申请
    elementquestion = Column(String(500), nullable=True, comment='提问文字描述')   # 实际展示给用户的问句
    elementnote = Column(String(500), nullable=True, comment='问题说明')           # 后台说明或帮助文本
    element_tip = Column(String(50), nullable=True, comment='问题提示文字')        # 前端 hover 提示内容

    # 关联信息
    catalogid = Column(String(50), nullable=True, comment='事项版本唯一标识')       # 关联 item_main_info.qaid 或版本ID
    preoptionguid = Column(String(50), nullable=True, comment='关联选项标识')       # 指向某个 answer option 的 guid（用于联动）
    wikiGuid = Column(String(50), nullable=True, comment='关联法律法规标识')       # 关联 law_info.rowguid
    tagguid = Column(String(50), nullable=True, comment='标签标识')               # 可用于分类打标

    # 控制属性
    multiselect = Column(String(10), nullable=True, comment='是否多选')            # '1'=是, '0'=否；或 'true'/'false'
    is_show = Column(String(2), nullable=True, comment='是否显示')                # '1'=显示, '0'=隐藏
    is_use = Column(String(2), nullable=True, comment='是否可用')                 # '1'=启用, '0'=停用

    # 高级逻辑规则（前端动态渲染使用）
    element_ldxs = Column(String(50), nullable=True, comment='问题联动显示/隐藏规则') # 如 JS 表达式或规则引擎 ID
    element_item = Column(String(50), nullable=True, comment='问题与事项关联规则')   # 复杂匹配逻辑，如 JSON 规则

    # 标识与排序
    element_eid = Column(String(50), nullable=True, comment='问题英文标识')         # 用于程序识别，如 field_business_type
    ordernum = Column(Integer, nullable=True, comment='排序号')                   # 前端展示顺序

    # 状态与时间
    state = Column(String(1), nullable=True, comment='状态')                       # '1'=有效, '0'=无效
    create_date = Column(Date, nullable=True, comment='创建时间')
    update_date = Column(Date, nullable=True, comment='更新时间')

    def __repr__(self):
        return f"<CatalogQxqInfo(elementname={self.elementname}, elementquestion='{self.elementquestion[:30]}...')>"