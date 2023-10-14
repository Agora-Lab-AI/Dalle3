This example demonstrates how to vectorize a PDF of the [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf) paper and setup a Zeta agent with rules and the `KnowledgeBase` tool to use it during conversations.

```python
import io
import requests
from zeta.engines import VectorQueryEngine
from zeta.loaders import PdfLoader
from zeta.structures import Agent
from zeta.tools import KnowledgeBaseClient
from zeta.utils import Chat

namespace = "attention"

response = requests.get("https://arxiv.org/pdf/1706.03762.pdf")
engine = VectorQueryEngine()

engine.vector_store_driver.upsert_text_artifacts(
    {
        namespace: PdfLoader().load(
            io.BytesIO(response.content)
        )
    }
)

kb_client = KnowledgeBaseClient(
    description="Contains information about the Attention Is All You Need paper. "
                "Use it to answer any related questions.",
    query_engine=engine,
    namespace=namespace
)

agent = Agent(
    tools=[kb_client]
)

Chat(agent).start()
```