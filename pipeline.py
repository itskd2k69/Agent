from agents import build_search_agent,build_reader_agent,writer_chain,critic_chain

def run_research_pipeline(topic : str) -> dict:

    state = {}

    # search agent working
    print("\n" + "="*50)
    print("step 1 - search agent is working...")
    print("=" *50)

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages" : [("user", f"Find recent, reliable and detailed information about: {topic}")]
    })

    state["search_results"] = search_result["messages"][-1].content

    print("\n search result", state['search_results'])

    # reader agent
    print("\n" + "="*50)
    print("step 2 - Reader agent is scraping from resources...")
    print("=" *50)

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}"
        )]
    })

    state["scraped_content"] = reader_result["messages"][-1].content

    print("\n scraped content \n", state['scraped_content'])

    # step 3 - writer chain
    print("\n" + "="*50)
    print("step 3 - Writer is drafting the report...")
    print("=" *50)

    research_combined = (
        f"SEARCH RESULTS : \n {state['search_results']} \n\n"
        f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic" : topic,
        "research" : research_combined
    })

    print("\n Final Reeport\n",state['report'])

    # critic report 
    print("\n" + "="*50)
    print("step 4 - critic is reviewing the report...")
    print("=" *50)

    state["feedback"]=critic_chain.invoke({
        "report" : state["report"]
    })

    print("\n critic report \n",state["feedback"])


    return state


if __name__ == "__main__":
    topic = input("\n Enter research topic : ")
    run_research_pipeline(topic)


# from agents import run_search, run_reader, writer_chain, critic_chain


# def extract_urls(search_text: str):
#     urls = []
#     for line in search_text.split("\n"):
#         if line.startswith("URL:"):
#             urls.append(line.replace("URL:", "").strip())
#     return urls


# def run_research_pipeline(topic: str) -> dict:

#     state = {}

#     # ===================== STEP 1 =====================
#     print("\n" + "=" * 50)
#     print("step 1 - search is working...")
#     print("=" * 50)

#     search_result = run_search(topic)

#     state["search_results"] = search_result

#     print("\n search result:\n", state["search_results"])

#     # ===================== STEP 2 =====================
#     print("\n" + "=" * 50)
#     print("step 2 - scraping top URL...")
#     print("=" * 50)

#     urls = extract_urls(state["search_results"])

#     if not urls:
#         print("No URLs found!")
#         state["scraped_content"] = ""
#     else:
#         content = run_reader(urls[0])
#         state["scraped_content"] = content

#     print("\n scraped content:\n", state["scraped_content"][:500])

#     # ===================== STEP 3 =====================
#     print("\n" + "=" * 50)
#     print("step 3 - Writer is drafting the report...")
#     print("=" * 50)

#     research_combined = (
#         f"SEARCH RESULTS:\n{state['search_results']}\n\n"
#         f"SCRAPED CONTENT:\n{state['scraped_content']}"
#     )

#     state["report"] = writer_chain.invoke({
#         "topic": topic,
#         "research": research_combined
#     })

#     print("\n Final Report:\n", state["report"])

#     # ===================== STEP 4 =====================
#     print("\n" + "=" * 50)
#     print("step 4 - critic is reviewing the report...")
#     print("=" * 50)

#     state["feedback"] = critic_chain.invoke({
#         "report": state["report"]
#     })

#     print("\n critic feedback:\n", state["feedback"])

#     return state


# if __name__ == "__main__":
#     topic = input("\n Enter research topic : ")
#     run_research_pipeline(topic)