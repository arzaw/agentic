def testmodel():
    import google.generativeai as genai
    genai.configure(api_key="AIzaSyBZL3ZOkZNW3y39q4FAjlvRz5KxD0udxPk")

    models=genai.list_models()
    for model in models:
        print(f"{model.name} - {model.supported_generation_methods}")

testmodel()