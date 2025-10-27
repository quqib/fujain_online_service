from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FAQInfo(Base):
    __tablename__ = 'faq_info'

    # 主键（建议数据库中设置 PRIMARY KEY）
    rowguid = Column(String(50), primary_key=True, nullable=True, comment='主键')

    # 问答内容
    question = Column(String(1000), nullable=True, comment='问题')
    answer = Column(String(2000), nullable=True, comment='解答')

    # 排序与标识
    ordernum = Column(Integer, nullable=True, comment='排序号')  # 前端展示顺序

    # 关联字段
    task_guid = Column(String(50), nullable=True, comment='事项唯一标识')     # 对应事项的 rowguid
    qaid = Column(String(50), nullable=True, comment='问答版本标识')          # 版本唯一标识
    task_code = Column(String(36), nullable=True, comment='实施编码')        # 实施编码，用于跨表关联
    ywcode = Column(String(50), nullable=True, comment='业务办理项编码')
    ywcode_ext = Column(String(100), nullable=True, comment='业务办理项扩展码')

    # 时间与状态
    create_date = Column(Date, nullable=True, comment='创建日期')
    state = Column(String(1), nullable=True, comment='状态')       # 如 '1'=有效, '0'=无效
    update_date = Column(Date, nullable=True, comment='更新时间')

    def __repr__(self):
        return f"<FAQInfo(question={self.question[:50]}..., task_code={self.task_code})>"