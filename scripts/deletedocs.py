import argparse
from azure.core.credentials import AzureKeyCredential
from azure.identity import AzureDeveloperCliCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes.models import *



def deletedocs():
    if args.verbose: print(f"Searching search index {args.index} exists")
    client = SearchClient(endpoint=f"https://{args.searchservice}.search.windows.net/",
                                    index_name=args.index,
                                    credential=search_creds)
    sourcefile_content = "iCims Training Manual v.7.pdf"
    search_query = f"sourcefile eq '{sourcefile_content}'"
    results = client.search(search_text="*", filter=search_query)
    document_keys_to_delete = [result["id"] for result in results]
    print("These are the keys to delete:")
    for result in document_keys_to_delete:
        print(result)
    key_field_name = "id"
    documents_to_delete = [{key_field_name: key} for key in document_keys_to_delete]
    confirmation = input("Do you want to continue? (Y/n): ").lower().strip()
    if confirmation == 'y' or confirmation == '':
        # actions = [{"__action_type": "delete", "id": key} for key in document_keys_to_delete]
        client.delete_documents(documents=documents_to_delete)
    else:
        print("You chose No.")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Delete documents ",
        epilog="Example: deletedocs.py '..\data\*' --storageaccount myaccount --container mycontainer --searchservice mysearch --index myindex -v"
        )
    parser.add_argument("files", help="Files to be processed")
    parser.add_argument("--category", help="Value for the category field in the search index for all sections indexed in this run")
    parser.add_argument("--skipblobs", action="store_true", help="Skip uploading individual pages to Azure Blob Storage")
    parser.add_argument("--storageaccount", help="Azure Blob Storage account name")
    parser.add_argument("--container", help="Azure Blob Storage container name")
    parser.add_argument("--storagekey", required=False, help="Optional. Use this Azure Blob Storage account key instead of the current user identity to login (use az login to set current user for Azure)")
    parser.add_argument("--tenantid", required=False, help="Optional. Use this to define the Azure directory where to authenticate)")
    parser.add_argument("--searchservice", help="Name of the Azure Cognitive Search service where content should be indexed (must exist already)")
    parser.add_argument("--index", help="Name of the Azure Cognitive Search index where content should be indexed (will be created if it doesn't exist)")
    parser.add_argument("--searchkey", required=False, help="Optional. Use this Azure Cognitive Search account key instead of the current user identity to login (use az login to set current user for Azure)")
    parser.add_argument("--openaiservice", help="Name of the Azure OpenAI service used to compute embeddings")
    parser.add_argument("--openaideployment", help="Name of the Azure OpenAI model deployment for an embedding model ('text-embedding-ada-002' recommended)")
    parser.add_argument("--novectors", action="store_true", help="Don't compute embeddings for the sections (e.g. don't call the OpenAI embeddings API during indexing)")
    parser.add_argument("--openaikey", required=False, help="Optional. Use this Azure OpenAI account key instead of the current user identity to login (use az login to set current user for Azure)")
    parser.add_argument("--remove", action="store_true", help="Remove references to this document from blob storage and the search index")
    parser.add_argument("--removeall", action="store_true", help="Remove all blobs from blob storage and documents from the search index")
    parser.add_argument("--localpdfparser", action="store_true", help="Use PyPdf local PDF parser (supports only digital PDFs) instead of Azure Form Recognizer service to extract text, tables and layout from the documents")
    parser.add_argument("--formrecognizerservice", required=False, help="Optional. Name of the Azure Form Recognizer service which will be used to extract text, tables and layout from the documents (must exist already)")
    parser.add_argument("--formrecognizerkey", required=False, help="Optional. Use this Azure Form Recognizer account key instead of the current user identity to login (use az login to set current user for Azure)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = parser.parse_args()

    # Use the current user identity to connect to Azure services unless a key is explicitly set for any of them
    azd_credential = AzureDeveloperCliCredential() if args.tenantid == None else AzureDeveloperCliCredential(tenant_id=args.tenantid, process_timeout=60)
    default_creds = azd_credential if args.searchkey == None or args.storagekey == None else None
    search_creds = default_creds if args.searchkey == None else AzureKeyCredential(args.searchkey)
    use_vectors = not args.novectors

    if not args.skipblobs:
        storage_creds = default_creds if args.storagekey == None else args.storagekey
    if not args.localpdfparser:
        # check if Azure Form Recognizer credentials are provided
        if args.formrecognizerservice == None:
            print("Error: Azure Form Recognizer service is not provided. Please provide formrecognizerservice or use --localpdfparser for local pypdf parser.")
            exit(1)
        formrecognizer_creds = default_creds if args.formrecognizerkey == None else AzureKeyCredential(args.formrecognizerkey)
    
    print(f"Deleting entries...")
    deletedocs()
