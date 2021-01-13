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
    result = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    await result.save()
    return result.id
