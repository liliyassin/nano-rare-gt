"""Build ROGDI recall cards, Anki deck, and exam PDFs.

This script is intentionally self-contained so the study artifacts can be
regenerated without network access or extra Python packages.
"""

from __future__ import annotations

import csv
import html
import json
import re
import sqlite3
import time
import zipfile
from dataclasses import dataclass
from hashlib import sha1
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "study"
DECK_NAME = "nano-rare GT::ROGDI source-audited recall"


@dataclass(frozen=True)
class Card:
    topic: str
    question: str
    answer: str


CARDS: list[Card] = [
    Card(
        "Core identity",
        "What disease is the ROGDI case study about?",
        "Kohlschutter-Tonz syndrome, also called amelocerebrohypohidrotic syndrome.",
    ),
    Card(
        "Core identity",
        "What is the Orphanet ID for the ROGDI/KTS disease case?",
        "ORPHA:1946.",
    ),
    Card(
        "Core identity",
        "What are the two OMIM identifiers used in the ROGDI audit?",
        "OMIM phenotype 226750 and OMIM gene 614574.",
    ),
    Card(
        "Core identity",
        "What is the correct gene symbol for the case study?",
        "ROGDI.",
    ),
    Card(
        "Core identity",
        "What is the correct UniProt accession for human ROGDI?",
        "Q9GZN7.",
    ),
    Card(
        "Core identity",
        "What is the recommended protein name for UniProt Q9GZN7?",
        "Protein rogdi homolog.",
    ),
    Card(
        "Core identity",
        "What are three aliases for ROGDI?",
        "KIAA0267, FLJ22386, and RAV2.",
    ),
    Card(
        "Core identity",
        "What chromosome location is listed for ROGDI?",
        "16p12.1.",
    ),
    Card(
        "Core identity",
        "What is the protein length of ROGDI?",
        "287 amino acids.",
    ),
    Card(
        "Core identity",
        "What is the approximate molecular weight of ROGDI?",
        "About 32.3 kDa, or 32,254 Da.",
    ),
    Card(
        "Core identity",
        "What is the approximate ROGDI amino-acid coding region length?",
        "About 861 bp, or 864 bp if the stop codon is included by convention.",
    ),
    Card(
        "Source verification",
        "Why is source verification the first step before scoring a gene therapy target?",
        "Because a wrong disease, gene, or protein identity poisons every downstream conclusion: cargo size, mechanism, potency assay, vector fit, and risk assessment.",
    ),
    Card(
        "Source verification",
        "Which source is used to confirm protein identity and sequence facts?",
        "UniProt. For ROGDI, the key accession is Q9GZN7.",
    ),
    Card(
        "Source verification",
        "Which source is used to anchor rare disease identity?",
        "Orphanet. For this case, the disease is ORPHA:1946.",
    ),
    Card(
        "Source verification",
        "Which source is used for disease and gene OMIM entries?",
        "OMIM. For ROGDI/KTS, phenotype 226750 and gene 614574 are used.",
    ),
    Card(
        "Source verification",
        "What live UniProt facts were checked for Q9GZN7?",
        "Primary accession, protein name, gene name, sequence length, molecular weight, and cross-references such as PDB, AlphaFoldDB, InterPro, and Pfam.",
    ),
    Card(
        "Disease biology",
        "What is the inheritance pattern of Kohlschutter-Tonz syndrome?",
        "Autosomal recessive.",
    ),
    Card(
        "Disease biology",
        "Why does autosomal recessive loss of function support gene addition?",
        "Because adding a working copy of the gene can, in principle, replace missing or reduced function.",
    ),
    Card(
        "Disease biology",
        "What are the three classic features of KTS described in the audit?",
        "Amelogenesis imperfecta, infantile or early-onset epilepsy, and intellectual disability or severe neurodevelopmental impairment.",
    ),
    Card(
        "Disease biology",
        "Name three additional clinical features reported in KTS.",
        "Spasticity, hypohidrosis or heat intolerance, and nephrocalcinosis in some patients.",
    ),
    Card(
        "Disease biology",
        "Why does the audit prioritize CNS rescue?",
        "Because epilepsy and neurodevelopmental impairment likely dominate morbidity and mortality.",
    ),
    Card(
        "Disease biology",
        "Why might dental disease be hard to reverse in KTS?",
        "Enamel is formed during a limited developmental window and does not remodel like bone once formed.",
    ),
    Card(
        "Protein function",
        "How should ROGDI be treated functionally for gene therapy planning?",
        "As a non-secreted intracellular scaffold or adaptor protein, not as a simple enzyme replacement target.",
    ),
    Card(
        "Protein function",
        "What two PDB structures are linked to human ROGDI?",
        "5XQH and 5XQI.",
    ),
    Card(
        "Protein function",
        "What domain or family annotations are listed for ROGDI?",
        "RAVE2/Rogdi, Rogdi_lz, InterPro IPR028241, and Pfam PF10259.",
    ),
    Card(
        "Protein function",
        "What 2025 biology connection is important for ROGDI?",
        "ROGDI is connected to Rabconnectin-3-associated V-ATPase biology.",
    ),
    Card(
        "Protein function",
        "Why does the Rabconnectin-3/V-ATPase link matter?",
        "It gives a plausible mechanism involving acidic organelles, lysosomes, synaptic vesicles, neurons, and enamel/mineralization biology.",
    ),
    Card(
        "Localization",
        "Is ROGDI secreted?",
        "No. ROGDI is treated as intracellular and non-secreted.",
    ),
    Card(
        "Localization",
        "Why does non-secreted localization make gene therapy harder?",
        "Because neighboring corrected cells are unlikely to rescue uncorrected cells by secreting the protein. The affected cells probably need direct transduction.",
    ),
    Card(
        "Localization",
        "What is cell-autonomous rescue?",
        "A therapeutic effect that requires correction inside the affected cell itself.",
    ),
    Card(
        "Localization",
        "What is cross-correction?",
        "Rescue of neighboring untransduced cells by a secreted therapeutic protein.",
    ),
    Card(
        "Localization",
        "Why is cross-correction expected to be low for ROGDI?",
        "Because ROGDI is not known to be secreted.",
    ),
    Card(
        "Localization",
        "Name three reported or annotated ROGDI localization contexts.",
        "Nuclear envelope, axon/dendrite/perikaryon, presynapse, synaptic vesicle context, or acidic organelle context.",
    ),
    Card(
        "Target tissues",
        "What is the highest-priority therapeutic tissue for the first ROGDI program?",
        "CNS neurons.",
    ),
    Card(
        "Target tissues",
        "Which tooth-development cell type matters for KTS dental disease?",
        "Ameloblasts, the cells responsible for enamel formation.",
    ),
    Card(
        "Target tissues",
        "Why is there a brain/teeth delivery mismatch?",
        "A CNS-directed route is not expected to robustly correct ameloblasts, and dental-directed delivery will not rescue CNS neurons.",
    ),
    Card(
        "AAV and cargo",
        "What is AAV?",
        "Adeno-associated virus, a small non-replicating viral vector commonly used for in vivo gene delivery.",
    ),
    Card(
        "AAV and cargo",
        "What practical AAV packaging limit is used in the audit?",
        "About 4.7 kb.",
    ),
    Card(
        "AAV and cargo",
        "Why does ROGDI pass the AAV cargo-size gate?",
        "Its coding sequence is about 861 bp, leaving large room for promoter, polyA, ITRs, and other regulatory elements within the AAV limit.",
    ),
    Card(
        "AAV and cargo",
        "What first-pass vector is recommended for the ROGDI CNS proof of concept?",
        "AAV9.",
    ),
    Card(
        "AAV and cargo",
        "Why is AAV9 considered relevant to ROGDI?",
        "It has clinical precedent for nervous-system exposure, especially early-life CNS-directed gene replacement.",
    ),
    Card(
        "AAV and cargo",
        "Does AAV9 precedent prove ROGDI efficacy?",
        "No. It only supports platform feasibility. ROGDI-specific success still requires direct neuronal transduction, correct localization, and valid potency assays.",
    ),
    Card(
        "Construct design",
        "What promoter is recommended for the first ROGDI CNS proof of concept?",
        "hSYN1, a compact human synapsin-1 promoter for neuron-biased expression.",
    ),
    Card(
        "Construct design",
        "Why use a neuron-biased promoter like hSYN1 first?",
        "It matches the CNS objective and may reduce unnecessary peripheral overexpression.",
    ),
    Card(
        "Construct design",
        "What cargo would the first-pass ROGDI construct carry?",
        "Sequence-verified human ROGDI Q9GZN7 cDNA.",
    ),
    Card(
        "Construct design",
        "What routes are considered for CNS-prioritized ROGDI delivery?",
        "Early-life systemic IV or intrathecal delivery, selected after biodistribution and toxicity comparison.",
    ),
    Card(
        "Potency assays",
        "Why is a simple enzyme activity assay not enough for ROGDI?",
        "ROGDI is not being treated as a simple catalytic enzyme. It likely works through localization, complex interaction, and organelle/synaptic biology.",
    ),
    Card(
        "Potency assays",
        "What should a ROGDI potency assay package measure?",
        "Expression, intracellular localization, Rabconnectin-3 or complex interaction, V-ATPase/acidification readouts, and cell-based rescue.",
    ),
    Card(
        "Potency assays",
        "What patient-cell model is proposed for early ROGDI testing?",
        "Patient-derived iPSC neurons, with ameloblast-lineage or dental organoid assays where possible.",
    ),
    Card(
        "Preclinical plan",
        "What is milestone 1 in the ROGDI preclinical strategy?",
        "Source-lock and construct design: reconfirm Q9GZN7, lock transcript/cDNA convention, sequence-verify cDNA, and avoid stale annotations.",
    ),
    Card(
        "Preclinical plan",
        "What is milestone 2 in the ROGDI preclinical strategy?",
        "Patient-cell models: generate disease-relevant cells, confirm reduced or absent ROGDI, and define disease phenotypes.",
    ),
    Card(
        "Preclinical plan",
        "What is milestone 3 in the ROGDI preclinical strategy?",
        "Vector expression and potency: produce AAV9-hSYN1-ROGDI, confirm expression/localization, measure mechanism-linked rescue, and compare doses.",
    ),
    Card(
        "Preclinical plan",
        "What is milestone 4 in the ROGDI preclinical strategy?",
        "Animal proof of concept: use a validated Rogdi-deficient model if available and assess biodistribution, expression, seizure burden, survival, behavior, and safety.",
    ),
    Card(
        "Preclinical plan",
        "What is milestone 5 in the ROGDI preclinical strategy?",
        "IND-enabling package: release assays, potency assays, GLP toxicology, biodistribution, and early regulator engagement.",
    ),
    Card(
        "Risks",
        "What is the risk called when AAV does not reach enough affected cells?",
        "Cell-autonomous delivery failure.",
    ),
    Card(
        "Risks",
        "How should cell-autonomous delivery failure be mitigated?",
        "Quantify direct neuronal transduction and do not assume cross-correction.",
    ),
    Card(
        "Risks",
        "What is the dental/CNS mismatch risk?",
        "A brain-focused therapy may not fix tooth enamel disease, and a dental-focused therapy will not rescue the brain.",
    ),
    Card(
        "Risks",
        "What is the main overexpression concern for ROGDI?",
        "Stoichiometric imbalance, mislocalization, or disrupted protein-complex assembly.",
    ),
    Card(
        "Risks",
        "What AAV safety issues should be monitored?",
        "Anti-AAV immunity, liver toxicity, CNS inflammation, and dorsal root ganglion toxicity.",
    ),
    Card(
        "Scoring",
        "Which ROGDI score is the strongest in the framework and why?",
        "Size compatibility, because the ROGDI coding sequence is very small compared with the AAV packaging limit.",
    ),
    Card(
        "Scoring",
        "What composite score does the deep-dive give ROGDI approximately?",
        "About 0.62 in the current unweighted v0.2 implementation.",
    ),
    Card(
        "Scoring",
        "What is the ROGDI gate status?",
        "PASS for size compatibility.",
    ),
    Card(
        "Scoring",
        "Why is tissue tropism not scored as very high for ROGDI?",
        "AAV9 can support a CNS strategy, but enamel-forming tissues remain hard to reach and timing-limited.",
    ),
    Card(
        "Go/no-go",
        "Name three green-light criteria for ROGDI.",
        "Confirmed Q9GZN7/ROGDI identity, correct expression/localization in patient neurons, mechanism-linked cell rescue, animal CNS benefit at tolerable dose, and regulatory acceptance of potency logic.",
    ),
    Card(
        "Go/no-go",
        "Name three kill criteria for ROGDI.",
        "Failure to express or localize ROGDI, no functional rescue despite expression, unacceptable toxicity, inadequate CNS biodistribution, or potency assays that cannot be linked to disease mechanism.",
    ),
    Card(
        "Reusable workflow",
        "What is the first reusable step when applying this framework to another disease?",
        "Lock the disease, gene, and protein identity using trusted source IDs before scoring or designing a vector.",
    ),
    Card(
        "Reusable workflow",
        "What key facts should be collected for any new disease?",
        "Disease ID, gene ID, protein ID, inheritance, mechanism, clinical features, target tissues, protein size, localization, secretion status, existing treatments, and source links.",
    ),
    Card(
        "Reusable workflow",
        "What is the main lesson of the corrected ROGDI audit?",
        "A small gene can still be technically demanding if the protein is intracellular, non-secreted, localization-sensitive, and affects hard-to-reach tissues.",
    ),
]


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def write_markdown_files(cards: list[Card]) -> None:
    qa_path = OUT / "ROGDI_recall_cards.md"
    questions_path = OUT / "ROGDI_recall_questions_exam.md"
    answers_path = OUT / "ROGDI_recall_answers_key.md"

    qa_lines = [
        "# ROGDI Recall Cards",
        "",
        "These cards are based on `docs/ROGDI-deep-dive.md` and focus on reusable gene-therapy framework knowledge.",
        "",
    ]
    q_lines = [
        "# ROGDI Recall Exam Questions",
        "",
        "Answer these without looking at the deep-dive file first.",
        "",
    ]
    a_lines = [
        "# ROGDI Recall Exam Answer Key",
        "",
        "Use this after attempting the questions.",
        "",
    ]

    for index, card in enumerate(cards, start=1):
        qa_lines.extend(
            [
                f"## {index}. {card.topic}",
                "",
                f"**Question:** {card.question}",
                "",
                f"**Answer:** {card.answer}",
                "",
            ]
        )
        q_lines.extend(
            [
                f"## Question {index}",
                "",
                card.question,
                "",
                "Answer:",
                "",
                "",
                "",
            ]
        )
        a_lines.extend(
            [
                f"## Question {index}",
                "",
                f"**Question:** {card.question}",
                "",
                f"**Answer:** {card.answer}",
                "",
            ]
        )

    qa_path.write_text("\n".join(qa_lines), encoding="utf-8")
    questions_path.write_text("\n".join(q_lines), encoding="utf-8")
    answers_path.write_text("\n".join(a_lines), encoding="utf-8")


def write_tsv(cards: list[Card]) -> None:
    path = OUT / "ROGDI_recall_anki_import.tsv"
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["Front", "Back", "Tags"])
        for card in cards:
            tags = "ROGDI nano-rare-GT " + re.sub(r"[^A-Za-z0-9]+", "_", card.topic).strip("_")
            writer.writerow([card.question, card.answer, tags])


BASE91 = list(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    "!#$%&()*+,-./:;<=>?@[]^_`{|}~"
)


def guid_for(text: str) -> str:
    number = int(sha1(text.encode("utf-8")).hexdigest(), 16)
    chars: list[str] = []
    while number:
        number, rem = divmod(number, len(BASE91))
        chars.append(BASE91[rem])
    return "".join(chars[:10])


def checksum(text: str) -> int:
    cleaned = re.sub(r"<[^>]+>", "", text)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return int(sha1(cleaned.encode("utf-8")).hexdigest()[:8], 16)


def write_anki_apkg(cards: list[Card]) -> None:
    apkg_path = OUT / "ROGDI_recall_anki_deck.apkg"
    now = int(time.time())
    deck_id = 1779277001
    model_id = 1779277002

    model = {
        str(model_id): {
            "id": model_id,
            "name": "ROGDI Basic Recall",
            "type": 0,
            "mod": now,
            "usn": -1,
            "sortf": 0,
            "did": deck_id,
            "tmpls": [
                {
                    "name": "Card 1",
                    "ord": 0,
                    "qfmt": '<div class="topic">{{Topic}}</div><div class="question">{{Front}}</div>',
                    "afmt": '{{FrontSide}}<hr id="answer"><div class="answer">{{Back}}</div>',
                    "did": None,
                    "bqfmt": "",
                    "bafmt": "",
                }
            ],
            "flds": [
                {"name": "Front", "ord": 0, "sticky": False, "rtl": False, "font": "Arial", "size": 20},
                {"name": "Back", "ord": 1, "sticky": False, "rtl": False, "font": "Arial", "size": 20},
                {"name": "Topic", "ord": 2, "sticky": False, "rtl": False, "font": "Arial", "size": 16},
            ],
            "css": (
                ".card { font-family: Arial; font-size: 20px; text-align: left; color: #111; background: white; } "
                ".topic { color: #666; font-size: 14px; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 0.04em; } "
                ".question { font-size: 22px; line-height: 1.35; } "
                ".answer { font-size: 20px; line-height: 1.45; }"
            ),
            "latexPre": "\\documentclass[12pt]{article}",
            "latexPost": "\\end{document}",
            "req": [[0, "any", [0]]],
            "tags": [],
            "vers": [],
        }
    }
    deck = {
        str(deck_id): {
            "id": deck_id,
            "name": DECK_NAME,
            "desc": "Recall questions from docs/ROGDI-deep-dive.md",
            "mod": now,
            "usn": -1,
            "lrnToday": [0, 0],
            "revToday": [0, 0],
            "newToday": [0, 0],
            "timeToday": [0, 0],
            "collapsed": False,
            "browserCollapsed": False,
            "dyn": 0,
            "conf": 1,
            "extendNew": 0,
            "extendRev": 0,
        }
    }
    dconf = {
        "1": {
            "id": 1,
            "name": "Default",
            "mod": 0,
            "usn": 0,
            "maxTaken": 60,
            "autoplay": True,
            "timer": 0,
            "replayq": True,
            "new": {
                "delays": [1.0, 10.0],
                "ints": [1, 4, 0],
                "initialFactor": 2500,
                "perDay": 20,
                "bury": True,
                "order": 1,
            },
            "rev": {"perDay": 200, "ease4": 1.3, "fuzz": 0.05, "minSpace": 1, "ivlFct": 1.0, "maxIvl": 36500, "bury": True},
            "lapse": {"delays": [10.0], "mult": 0.0, "minInt": 1, "leechFails": 8, "leechAction": 0},
            "dyn": False,
        }
    }
    conf = {
        "nextPos": 1,
        "estTimes": True,
        "activeDecks": [deck_id],
        "sortType": "noteFld",
        "timeLim": 0,
        "sortBackwards": False,
        "addToCur": True,
        "curDeck": deck_id,
        "newBury": True,
        "newSpread": 0,
        "dueCounts": True,
        "curModel": model_id,
    }

    with TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "collection.anki2"
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.executescript(
            """
            CREATE TABLE col (
                id              integer primary key,
                crt             integer not null,
                mod             integer not null,
                scm             integer not null,
                ver             integer not null,
                dty             integer not null,
                usn             integer not null,
                ls              integer not null,
                conf            text not null,
                models          text not null,
                decks           text not null,
                dconf           text not null,
                tags            text not null
            );
            CREATE TABLE notes (
                id              integer primary key,
                guid            text not null,
                mid             integer not null,
                mod             integer not null,
                usn             integer not null,
                tags            text not null,
                flds            text not null,
                sfld            integer not null,
                csum            integer not null,
                flags           integer not null,
                data            text not null
            );
            CREATE TABLE cards (
                id              integer primary key,
                nid             integer not null,
                did             integer not null,
                ord             integer not null,
                mod             integer not null,
                usn             integer not null,
                type            integer not null,
                queue           integer not null,
                due             integer not null,
                ivl             integer not null,
                factor          integer not null,
                reps            integer not null,
                lapses          integer not null,
                left            integer not null,
                odue            integer not null,
                odid            integer not null,
                flags           integer not null,
                data            text not null
            );
            CREATE TABLE revlog (
                id              integer primary key,
                cid             integer not null,
                usn             integer not null,
                ease            integer not null,
                ivl             integer not null,
                lastIvl         integer not null,
                factor          integer not null,
                time            integer not null,
                type            integer not null
            );
            CREATE TABLE graves (
                usn             integer not null,
                oid             integer not null,
                type            integer not null
            );
            """
        )
        cur.execute(
            "INSERT INTO col VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                1,
                now // 86400,
                now,
                now,
                11,
                0,
                0,
                0,
                json.dumps(conf),
                json.dumps(model),
                json.dumps(deck),
                json.dumps(dconf),
                "{}",
            ),
        )

        note_base = 1779278000000
        card_base = 1779279000000
        for index, card in enumerate(cards, start=1):
            nid = note_base + index
            cid = card_base + index
            fields = "\x1f".join(
                [
                    html.escape(card.question),
                    html.escape(card.answer),
                    html.escape(card.topic),
                ]
            )
            cur.execute(
                "INSERT INTO notes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    nid,
                    guid_for(card.question + card.answer),
                    model_id,
                    now,
                    -1,
                    " ROGDI nano_rare_GT ",
                    fields,
                    html.escape(card.question),
                    checksum(card.question),
                    0,
                    "",
                ),
            )
            cur.execute(
                "INSERT INTO cards VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    cid,
                    nid,
                    deck_id,
                    0,
                    now,
                    -1,
                    0,
                    0,
                    index,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    "",
                ),
            )

        conn.commit()
        conn.close()

        media_path = Path(temp_dir) / "media"
        media_path.write_text("{}", encoding="utf-8")
        with zipfile.ZipFile(apkg_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.write(db_path, "collection.anki2")
            archive.write(media_path, "media")


class PdfWriter:
    def __init__(self, title: str) -> None:
        self.title = title
        self.pages: list[list[str]] = []

    @staticmethod
    def _escape(text: str) -> str:
        return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")

    def add_page(self, lines: list[str]) -> None:
        self.pages.append(lines)

    def write(self, path: Path) -> None:
        objects: list[bytes] = []
        kids: list[int] = []
        font_obj = 4
        for page_lines in self.pages:
            content_lines = ["BT", "/F1 11 Tf", "14 TL", "72 740 Td"]
            first = True
            for line in page_lines:
                if not first:
                    content_lines.append("T*")
                first = False
                if line == "":
                    content_lines.append("T*")
                else:
                    content_lines.append(f"({self._escape(line)}) Tj")
            content_lines.append("ET")
            stream = "\n".join(content_lines).encode("latin-1", errors="replace")
            content_obj = len(objects) + 1
            objects.append(
                b"<< /Length "
                + str(len(stream)).encode()
                + b" >>\nstream\n"
                + stream
                + b"\nendstream"
            )
            page_obj = len(objects) + 1
            kids.append(page_obj)
            objects.append(
                (
                    f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
                    f"/Resources << /Font << /F1 {font_obj} 0 R >> >> "
                    f"/Contents {content_obj} 0 R >>"
                ).encode()
            )

        catalog = b"<< /Type /Catalog /Pages 2 0 R >>"
        pages = f"<< /Type /Pages /Kids [{' '.join(f'{kid} 0 R' for kid in kids)}] /Count {len(kids)} >>".encode()
        info = f"<< /Title ({self._escape(self.title)}) /Creator (nano-rare-gt study builder) >>".encode()
        font = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"
        ordered = [catalog, pages, info, font] + objects

        output = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        offsets = [0]
        for number, obj in enumerate(ordered, start=1):
            offsets.append(len(output))
            output.extend(f"{number} 0 obj\n".encode())
            output.extend(obj)
            output.extend(b"\nendobj\n")
        xref_start = len(output)
        output.extend(f"xref\n0 {len(ordered) + 1}\n".encode())
        output.extend(b"0000000000 65535 f \n")
        for offset in offsets[1:]:
            output.extend(f"{offset:010d} 00000 n \n".encode())
        output.extend(
            (
                f"trailer << /Size {len(ordered) + 1} /Root 1 0 R /Info 3 0 R >>\n"
                f"startxref\n{xref_start}\n%%EOF\n"
            ).encode()
        )
        path.write_bytes(bytes(output))


def wrap(text: str, width: int = 86) -> list[str]:
    words = clean_text(text).split(" ")
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else current + " " + word
        if len(candidate) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def paginate(blocks: list[list[str]], title: str) -> list[list[str]]:
    pages: list[list[str]] = []
    page: list[str] = [title, ""]
    max_lines = 46
    for block in blocks:
        if len(page) + len(block) + 1 > max_lines:
            pages.append(page)
            page = [title + " (continued)", ""]
        page.extend(block)
        page.append("")
    if page:
        pages.append(page)
    for page_number, page_lines in enumerate(pages, start=1):
        page_lines.append("")
        page_lines.append(f"Page {page_number}")
    return pages


def write_pdfs(cards: list[Card]) -> None:
    question_blocks: list[list[str]] = []
    answer_blocks: list[list[str]] = []
    for index, card in enumerate(cards, start=1):
        question_blocks.append([f"{index}. {card.question}", "Answer:", ""])
        answer_blocks.append(
            wrap(f"{index}. {card.question}") + wrap(f"Answer: {card.answer}") + [f"Topic: {card.topic}"]
        )

    question_pdf = PdfWriter("ROGDI Recall Exam Questions")
    for page in paginate(question_blocks, "ROGDI Recall Exam Questions"):
        question_pdf.add_page(page)
    question_pdf.write(OUT / "ROGDI_recall_questions_exam.pdf")

    answer_pdf = PdfWriter("ROGDI Recall Exam Answer Key")
    for page in paginate(answer_blocks, "ROGDI Recall Exam Answer Key"):
        answer_pdf.add_page(page)
    answer_pdf.write(OUT / "ROGDI_recall_answers_key.pdf")


def main() -> None:
    OUT.mkdir(exist_ok=True)
    cards = [Card(c.topic, clean_text(c.question), clean_text(c.answer)) for c in CARDS]
    write_markdown_files(cards)
    write_tsv(cards)
    write_anki_apkg(cards)
    write_pdfs(cards)
    print(f"Built {len(cards)} cards in {OUT}")


if __name__ == "__main__":
    main()
