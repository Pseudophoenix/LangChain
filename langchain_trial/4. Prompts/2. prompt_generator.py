from langchain_core.prompts import PromptTemplate
template=PromptTemplate(
            template="""
            Please summarize the research paper titled "{paper_input}" with the following specifications:
            Explaination Style:{style_input}
            Explaination Lenght:{length_input}
            1. Mathematical Details:
                - include relevant mathematical equations if present in the paper.
                - explain the mathematical concepts using simple, intuitive code snippets where applicable!
            2. Analogies:
                - use relatable analogies to simplify complex ideas.
            If certain information is not available in the paper, respond with "Insufficient Information available" instead of guessing. 
            Ensure the summary is clear, accurate and aligned with the provided style and length
            """,
            input_variable=["paper_input","style_input","length_input"]
)
template.save('template.json')