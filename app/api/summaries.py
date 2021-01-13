#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List

from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema
from app.models.tortoise import SummarySchema

router = APIRouter()


@router.get("/", response_model=List[SummarySchema])
async def read_all_summaries() -> list[SummarySchema]:
    response_object = await crud.get_all()

    if not response_object:
        raise HTTPException(status_code=404, detail="Summary not found")

    return response_object


@router.get("/{id}", response_model=SummarySchema)
async def read_summary(id: int) -> SummarySchema:
    response_object = await crud.get(id)

    if not response_object:
        raise HTTPException(status_code=404, detail="Summary not found")

    return response_object


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    summary_id = await crud.post(payload)

    response_object = {"id": summary_id, "url": payload.url}

    return response_object
