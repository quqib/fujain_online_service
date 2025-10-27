from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProcessFlowInfo(Base):
    __tablename__ = 'process_flow_info'

    # 主键（建议数据库中设置 PRIMARY KEY）
    rowguid = Column(String(50), primary_key=True, nullable=True, comment='主键')

    # 关联字段
    task_guid = Column(String(50), nullable=True, comment='事项主键')               # 关联 item_main_info.rowguid
    activityid = Column(String(50), nullable=True, comment='环节版本标识')         # 环节的版本唯一标识
    activityname = Column(String(50), nullable=True, comment='环节名称')           # 如：受理、审核、办结

    # 办理时限
    handle_timelimit = Column(Integer, nullable=True, comment='办理期限')          # 数值，如 3、5
    handle_timelimit_type = Column(String(1), nullable=True, comment='办理期限单位') # '1'=工作日, '2'=自然日, '3'=小时 等

    # 职能与标准
    activityduty = Column(String(200), nullable=True, comment='职能描述')          # 该环节的职责说明
    handlelink_examine = Column(String(300), nullable=True, comment='办理流程环节审批标准')  # 审核要点或标准描述

    # 排序与结果
    ordernum = Column(Integer, nullable=True, comment='排序号')                   # 流程中的顺序，用于前端展示
    handle_result = Column(String(1000), nullable=True, comment='办理结果')        # 本环节产生的结果描述

    # 状态与时间
    state = Column(String(1), nullable=True, comment='状态')                       # '1'=有效, '0'=无效
    create_date = Column(Date, nullable=True, comment='创建时间')
    update_date = Column(Date, nullable=True, comment='更新时间')

    def __repr__(self):
        return f"<ProcessFlowInfo(activityname={self.activityname}, ordernum={self.ordernum})>"