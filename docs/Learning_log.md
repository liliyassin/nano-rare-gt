# TERM: Orphanet

## Plain English
Database of rare diseases.

## Why it matters
Used to identify diseases and associated genes.

## Input
Disease names.

## Output
Disease IDs, genes, prevalence info.

## Used in pipeline
Disease discovery stage.

## How to verify manually
Search disease directly on orphanet website.

## Useful links
https://www.orpha.net/

## What I still don't understand
Difference between Orpha ID and OMIM ID.


Your ROGDI case study has a major identity error still spread through the repo.
    
    A live UniProt check says:
    
    ROGDI → Q9GZN7, ROGDI_HUMAN, “Protein rogdi homolog”, 287 aa
    
    But lots of your files still say:
    
    ROGDI / GMPR2 → Q9P2T1, 348 aa, GMP reductase 2
    
    That older mapping is wrong for ROGDI. It poisons the deep dive, fixture, tests, generated reports, vector sizing, homology logic, and the biological interpretation.
    
    So your next move is not “build more pipeline”. Your next move is:
    
    Stop expanding. Stabilise the scientific truth layer first.
    
    How to approach the whole project
    
    Think of nano-rare-gt as having two separate layers:
    
    1. Science truth layer
    This is the manually verified knowledge base:
    - What disease is this?
    - What gene actually causes it?
    - Which UniProt accession is correct?
    - What does the protein actually do?
    - Which tissues matter?
    - Is AAV feasible?
    - What are the delivery paradoxes?
    - What evidence supports each claim?
    
    2. Software automation layer
    This is the code that turns verified facts into repeatable outputs:
    - Pydantic models
    - database storage
    - API clients
    - scoring engine
    - report renderer
    - CLI
    
    Right now, the software layer is healthier than the science layer. The code passes tests, but some tests are passing because they assert incorrect old facts. That means “green tests” are not enough.
    
    Your project should now proceed like this:
    
    Phase A: ROGDI manual truth audit
    Before more coding, manually rebuild the ROGDI case study from source links.
    
    Phase B: Correct the project’s golden fixture
    The fixture should become the single truth source for ROGDI. Tests should verify the corrected facts.
    
    Phase C: Regenerate reports
    Only after the fixture is corrected should the report and protocol be trusted.
    
    Phase D: Build pipeline modules
    Once ROGDI is scientifically clean, then add Orphanet, OMIM, UniProt, vector, homology, and scoring automation.