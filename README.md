# Chatbot BSCCS103 Ethics and Computer Law
- BSCCS103 Ethics and Computer Law จริยธรรมและกฎหมายคอมพิวเตอร์

## สามารถใช้งานได้จาก 
Deployment on [streamlit](https://jeerasakananta-chatbot-bsccs103-ethics-and-computer--app-vdrxa6.streamlit.app/)

## วิธีการใช้งานพัฒนา  
- สร้าง environment ด้วย poetry 
```bash
poetry install
```
- การใช้งาน  env  
```bash
poetry shell
```
เรียกใช้งาน  app.py ด้วย  streamlit 
```bash
streamlit run app.py 
```

## drigram
```mermaid
graph TD
    A[Start] --> B[Load Environment Variables]
    B --> C[Initialize OpenAI Client]
    C --> D[Define get_openai_response Function]
    D --> E[Streamlit App Setup]
    E --> F[Initialize Chat History]
    F --> G[Display Chat History]
    G --> H{User Input?}
    H -->|Yes| I[Add User Message to Chat History]
    I --> J[Get OpenAI Response]
    J --> K[Add Assistant Response to Chat History]
    K --> G
    H -->|No| L[End]
```
- Sequence Diagram
```mermaid
sequenceDiagram
    participant User
    participant StreamlitApp
    participant OpenAIAPI
    participant SessionState

    User->>StreamlitApp: Enters input (prompt)
    StreamlitApp->>SessionState: Append user message to chat history
    StreamlitApp->>OpenAIAPI: Call get_openai_response(prompt)
    OpenAIAPI-->>StreamlitApp: Return response
    StreamlitApp->>SessionState: Append assistant response to chat history
    StreamlitApp-->>User: Display updated chat history
```

1. พิมข้อความของคุณ

## maintainer by
- Delopment By  Jeerasak Ananta SS4 CS  RMUTL
