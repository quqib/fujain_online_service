from sqlalchemy import Column, String, Integer, Date, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FeeItemInfo(Base):
    __tablename__ = 'feeitem_info'

    # 主键（建议数据库中设置为 PRIMARY KEY）
    rowguid = Column(String(50), primary_key=True, nullable=True, comment='主键')

    # 收费基本信息
    fee_name = Column(String(200), nullable=True, comment='收费项目名称')
    fee_stand = Column(String(2000), nullable=True, comment='收费标准')  # 字符串形式存储标准描述
    by_law = Column(LargeBinary, nullable=True, comment='收费依据')       # BLOB，可能包含富文本或长文本依据
    is_desc = Column(String(2), nullable=True, comment='是否允许减免')     # 如 '1' 是，'0' 否
    desc_explain = Column(String(2000), nullable=True, comment='允许减免依据')
    remark = Column(String(1000), nullable=True, comment='备注')

    # 排序与标识
    ordernum = Column(Integer, nullable=True, comment='排序号')  # 前端展示顺序

    # 关联字段
    task_guid = Column(String(50), nullable=True, comment='事项唯一标识')        # 关联事项主键
    chargeid = Column(String(50), nullable=True, comment='收费版本标识')         # 版本唯一标识
    task_code = Column(String(36), nullable=True, comment='实施编码')           # 实施编码，用于关联事项
    ywcode = Column(String(50), nullable=True, comment='业务办理项编码')
    ywcode_ext = Column(String(100), nullable=True, comment='业务办理项扩展码')

    # 时间与状态
    create_date = Column(Date, nullable=True, comment='创建日期')
    state = Column(String(1), nullable=True, comment='状态')         # 如 '1'=有效, '0'=无效
    update_date = Column(Date, nullable=True, comment='更新时间')

    def __repr__(self):
        return f"<FeeItemInfo(fee_name={self.fee_name}, task_code={self.task_code})>"