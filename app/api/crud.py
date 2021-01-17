#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Optional

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries


async def get(id: int) -> Optional[dict]:
    result = await TextSummary.filter(id=id).first().values()
    if result:
        return result[0]
    return None


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    await summary.save()
    return summary.id


async def delete(id: int) -> int:
    summary = await TextSummary.filter(id=id).first().delete()
    return summary
