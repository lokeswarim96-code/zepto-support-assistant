\# Zepto Support Assistant



\## Overview



A customer support assistant built using LangGraph, ChromaDB, and FastAPI.



The system retrieves relevant information from the support-document corpus and generates an answer using the configured LLM. The default configuration supports MOCK\_LLM for local testing.



\## Pipeline Architecture



User Question

&#x20;    |

&#x20;    v

FastAPI /ask endpoint

&#x20;    |

&#x20;    v

LangGraph workflow

&#x20;    |

&#x20;    +--> Query processing

&#x20;    |

&#x20;    +--> ChromaDB retrieval

&#x20;    |

&#x20;    +--> Relevant support-document chunks

&#x20;    |

&#x20;    +--> Answer generation

&#x20;    |

&#x20;    v

Structured response

&#x20;    |

&#x20;    v

User



\## Corpus



The `docs/` directory contains the support knowledge-base documents:



\- doc\_01.txt

\- doc\_02.txt

\- doc\_03.txt

\- doc\_04.txt

\- doc\_05.txt

\- doc\_06.txt

\- doc\_07.txt

\- doc\_08.txt



\## Ingestion



Run:



```bash

python ingest.py

