from sqlalchemy import Column, String, Date, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class LawInfo(Base):
    __tablename__ = 'law_info'

    # 主键（建议数据库中设置 PRIMARY KEY）
    rowguid = Column(String(50), primary_key=True, nullable=True, comment='主键')

    # 法律法规基本信息
    wikiname = Column(String(500), nullable=True, comment='法律法规名称')         # 完整名称，如《中华人民共和国行政许可法》
    law_content_tk = Column(String(50), nullable=True, comment='相关法条')        # 如 "第十八条"、"第三十二条第一款"
    law_content_xx = Column(LargeBinary, nullable=True, comment='相关法条内容')   # BLOB 类型，存储富文本或长文本内容（如 HTML 或 Markdown）

    # 颁布与实施信息
    issue_date = Column(Date, nullable=True, comment='颁布日期')                 # 法规发布日期
    execute_date = Column(Date, nullable=True, comment='实施日期')               # 法规生效日期
    issue_unit = Column(String(50), nullable=True, comment='颁布单位')           # 如：国务院、国家市场监督管理总局

    # 适用范围与描述
    applicable_scope = Column(String(500), nullable=True, comment='适用范围')     # 如：全国、特定行业
    description = Column(String(500), nullable=True, comment='描述')              # 简要说明该法规的作用
    remark = Column(String(500), nullable=True, comment='备注')                  # 其他补充信息

    # 来源与引用
    quoteurl = Column(String(200), nullable=True, comment='依据链接')            # 官方原文链接
    create_org = Column(String(50), nullable=True, comment='录入单位')           # 数据录入的机构名称

    # 时间与状态
    create_date = Column(Date, nullable=True, comment='创建日期')
    state = Column(String(1), nullable=True, comment='状态')                     # '1'=有效, '0'=无效
    update_date = Column(Date, nullable=True, comment='更新时间')

    def __repr__(self):
        return f"<LawInfo(wikiname={self.wikiname[:30]}..., issue_unit={self.issue_unit})>"