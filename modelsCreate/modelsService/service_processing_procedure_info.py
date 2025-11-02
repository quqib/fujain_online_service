"""
业务办理-办理流程表
"""
import uuid
from sqlalchemy import Column, String, CHAR, Text, DateTime, func, ForeignKey
from modelsCreate.base import Base


class ServiceProcessingProcedureInfo(Base):
    __tablename__ = 'service_processing_procedure_info'

    # 主键：使用 CHAR(36) 存储 UUID 字符串
    rowguid = Column(
        CHAR(36),  # 在数据库中存储为 CHAR(36)
        primary_key=True,
        default=lambda: str(uuid.uuid4()),  # 自动生成 UUID 字符串
        nullable=False,
        comment='主键，UUID 自动生成'
    )

    # 外键：关联到 service_basic_information_info 表的 rowguid
    basic_info_rowguid = Column(
        CHAR(36),
        ForeignKey('service_basic_information_info.rowguid', ondelete='CASCADE'),
        nullable=False,
        comment='关联 service_basic_information_info 表的主键'
    )

    # 办理流程
    procedure_name = Column(String(255), nullable=True, comment='办理流程')

    # 步骤类型
    step_type = Column(String(500), nullable=True, comment='步骤类型')

    # 办理人 / 岗位（可以是角色或具体人员）
    handler = Column(String(255), nullable=True, comment='办理人')

    # 办理时限（如“1工作日”、“即时办结”等描述性内容）
    handling_time_limit = Column(String(50), nullable=True, comment='办理时限')

    # 审查标准
    review_criteria = Column(Text, nullable=True, comment='审查标准')

    # 办理结果（如“通过”、“退回补正”、“不予受理”等）
    handling_result = Column(String(500), nullable=True, comment='办理结果')

    # 创建时间
    create_date = Column(DateTime, nullable=True, default=func.current_timestamp(), comment='创建时间')

    def __repr__(self):
        return f"<ProcessingProcedureStep(procedure_name='{self.procedure_name}', step_type='{self.step_type}', item_code='{self.item_code}')>"