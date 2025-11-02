"""
业务办理-网上办理信息表
"""
import uuid
from sqlalchemy import Column, String, CHAR, DateTime, func, ForeignKey
from modelsCreate.base import Base


class ServiceOnlineProcessingInfo(Base):
    __tablename__ = 'service_online_processing_info'

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
    # 是否涉及(0-否 1-是)
    does_it_involve = Column(String(2), nullable=True, comment='是否涉及')

    # 网上申请方式（如“政务服务网”、“闽政通APP”、“部门自建系统”等）
    online_application_method = Column(String(500), nullable=True, comment='网上申请方式')

    # 账户要求（如“需实名认证”、“需L3级账户”等）
    account_requirements = Column(String(500), nullable=True, comment='账户要求')

    # 承诺到窗口最多次数说明（如“全程网办，最多跑0次”或“材料预审后现场核验，最多跑1次”）
    max_visit_commitment = Column(String(500), nullable=True, comment='承诺到窗口最多次数说明')

    # 创建时间
    create_date = Column(DateTime, nullable=True, default=func.current_timestamp(), comment='创建时间')

    def __repr__(self):
        return f"<OnlineServiceInfo(item_code='{self.item_code}', online_application_method='{self.online_application_method}')>"