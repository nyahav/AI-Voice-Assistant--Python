from __future__ import annotations
from livekit.agents import (
    AutoSubscribe,
    JobContext,
    WorkerOptions,
    cli,
    llm
)
from livekit.agents.multimodal import (
    MultimodalAgent,
    
)
from livekit.plugins import openai
from api import AssistantFnc
from dotenv import load_dotenv
import os

load_dotenv()

async def entrypoint(ctx: JobContext):
    await ctx.connect(auto_subscribe=AutoSubscribe.SUBSCRIBE_ALL)
    await ctx.wait_for_participant()
    
    model = openai.realtime.RealtimeModel(
        instructions= "",
        voice="shimmer",
        temperature=0.8,
        modalities=["audio","text"]
    )
    
    assistant_fnc = AssistantFnc()
    assistant = MultimodalAgent(
        model=model,
        fnc_ctx=assistant_fnc
    )
    assistant.start(ctx.room)