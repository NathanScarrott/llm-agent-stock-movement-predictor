# Project Title: Sentiment-Augmented Stock Prediction with Agentic AI

## Objective
Evaluate whether real-time sentiment data from news and social media improves stock price prediction compared to using price data alone. Leverage a decision-making agent to coordinate data ingestion, sentiment analysis, and prediction.

## Step 1: Data Ingestion

### 1.1 Sentiment Data Pipeline
- Collect sentiment-rich text from sources like Twitter, Reddit, and Yahoo Finance.
- Use APIs or scraping tools with time-stamped storage.
- Save raw text for each time interval (e.g. hourly/daily).
- Questions:
  - Should ingestion be real-time or batch?
  - Should the agent pull or receive data automatically?

### 1.2 Stock Price Data Pipeline
- Ingest historical and live price data for a selected stock (AAPL).
- Optionally collect multiple stocks for generalisation.
- Sync time intervals with sentiment data.

## Step 2: Sentiment Processing

- Apply sentiment analysis models (VADER, FinBERT, or custom LLM-based).
- Extract numeric sentiment features per time window.
- Store features alongside text metadata.
- Optionally, allow the agent to select which model to use.

## Step 3: Feature Engineering

- Combine price features (technical indicators) with sentiment features.
- Align features chronologically and ensure no leakage.
- Create multiple datasets:
  - Price-only
  - Price + Sentiment
- Include contextual features (e.g. trading volume, volatility).

## Step 4: Predictive Modelling

- Train baseline ML models on price-only features (e.g. Random Forest, XGBoost, or LSTM).
- Train equivalent models with sentiment features added.
- Compare performance (AUC, accuracy, precision/recall).
- Optionally, evaluate using walk-forward validation or backtesting.

## Step 5: LLM Agent Design

### 5.1 Agent Functionality
- Fetch and process new data
- Monitor for drift or anomalies
- Choose which model to use for predictions
- Summarise outputs and confidence
- Log reasoning and decision process

### 5.2 Agent Tooling
- Tools: sentiment scorer, model selector, forecasting module, visualiser
- Framework: custom or LangChain-based
- Implement memory or intermediate state tracking

## Step 6: Evaluation and Interpretation

- Evaluate model performance with vs without sentiment.
- Evaluate agent's decision-making accuracy and success rate.
- Conduct case studies where sentiment made a difference.
- Data drift detector.
- Explore failure cases and suggest improvements.

## Step 7: Final Deliverables

- Notebook/Script pipeline end-to-end
- Visualisations of performance and impact of sentiment
- Documentation of methodology and agent behaviour
- Reflections on what you learned about sentiment and market prediction

## Success Criteria

- You can explain the role of sentiment in your model.
- The agent coordinates meaningful components of the pipeline.
- You've explored tradeoffs and made realistic conclusions.

