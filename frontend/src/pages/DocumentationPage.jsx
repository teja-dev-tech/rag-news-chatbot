import { Link } from 'react-router-dom';
import { ArrowLeft, BookOpen, Code, Lightbulb, FileText, Layers, MessageSquare, Database, Cpu, Search } from 'lucide-react';

export default function DocumentationPage() {
  return (
    <div className="max-w-4xl mx-auto p-6 text-left">
      <div className="mb-8">
        <Link to="/" className=" no-underline inline-flex items-center text-blue-600 hover:text-blue-800">
          <ArrowLeft className="w-4 h-4 mr-2" />
          Back to Chat
        </Link>
      </div>
      
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold text-gray-900 mb-4">Documentation</h1>
        <p className="text-xl text-gray-600 max-w-3xl mx-auto">
          Learn how to use the RAG Chatbot and understand its architecture
        </p>
      </div>
      
      <div className="space-y-12">
        {/* Overview Section */}
        <section className="bg-white rounded-xl shadow-sm p-6 ">
          <div className="flex items-center mb-6">
            <Layers className="w-6 h-6 text-blue-600 mr-3" />
            <span style={{ whiteSpace: 'pre' }}>   </span>
            <h2 className="text-2xl font-semibold text-gray-900">Overview</h2>
          </div>
          
          <div className="prose max-w-none text-gray-700 space-y-4">
            <p>
              The RAG (Retrieval-Augmented Generation) Chatbot is an AI-powered assistant that combines 
              the power of large language models with external knowledge retrieval to provide accurate 
              and contextual responses to user queries.
            </p>
            
            <div className="grid md:grid-cols-2 gap-6 mt-6">
              <div className="bg-blue-50 p-4 rounded-lg">
                <div className="flex items-center mb-2">
                  <Search className="w-5 h-5 text-blue-600 mr-2" />
                  <span style={{ whiteSpace: 'pre' }}>   </span>
                  <h3 className="font-medium">Knowledge Retrieval</h3>
                </div>
                <p className="text-sm text-gray-600">
                  Efficiently retrieves relevant information from a curated knowledge base of articles.
                </p>
              </div>
              
              <div className="bg-blue-50 p-4 rounded-lg">
                <div className="flex items-center mb-2">
                  <MessageSquare className="w-5 h-5 text-blue-600 mr-2" />
                  <span style={{ whiteSpace: 'pre' }}>   </span>
                  <h3 className="font-medium">Contextual Responses</h3>
                </div>
                <p className="text-sm text-gray-600">
                  Generates natural, context-aware responses based on retrieved information.
                </p>
              </div>
            </div>
          </div>
        </section>
        
        {/* How It Works Section */}
        <section className="bg-white rounded-xl shadow-sm p-6">
          <div className="flex items-center mb-4">
            <Cpu className="w-6 h-6 text-blue-600 mr-3" />
            <span style={{ whiteSpace: 'pre' }}>   </span>
            <h2 className="text-2xl font-semibold text-gray-900">How It Works</h2>
          </div>
          
          <div className="space-y-6">
            <div className="flex">
              <div className="flex flex-col items-center mr-4">
                <div className="flex items-center justify-center w-8 h-8 rounded-full bg-blue-100 text-blue-600 font-medium ">1</div>
                <div className="w-px h-full bg-gray-200"></div>
              </div>
              <div className="pb-6">
                <h3 className="font-medium text-gray-900 mb-1">Query Processing</h3>
                <p className="text-gray-600">Your question is analyzed to understand the intent and key concepts.</p>
              </div>
            </div>
            
            <div className="flex">
              <div className="flex flex-col items-center mr-4">
                <div className="flex items-center justify-center w-8 h-8 rounded-full bg-blue-100 text-blue-600 font-medium ">2</div>
                <div className="w-px h-full bg-gray-200"></div>
              </div>
              <div className="pb-6">
                <h3 className="font-medium text-gray-900 mb-1">Knowledge Retrieval</h3>
                <p className="text-gray-600">The system searches through the knowledge base for relevant information.</p>
              </div>
            </div>
            
            <div className="flex">
              <div className="flex flex-col items-center mr-4">
                <div className="flex items-center justify-center w-8 h-8 rounded-full bg-blue-100 text-blue-600 font-medium">3</div>
              </div>
              <div>
                <h3 className="font-medium text-gray-900 mb-1">Response Generation</h3>
                <p className="text-gray-600">A response is generated using the retrieved information and presented to you.</p>
              </div>
            </div>
          </div>
        </section>
        
        {/* API Reference */}
        <section className="bg-white rounded-xl shadow-sm p-6 ">
          <div className="flex items-center mb-6">
            <Code className="w-6 h-6 text-blue-600 mr-3" />
            <span style={{ whiteSpace: 'pre' }}>   </span>
            <h2 className="text-2xl font-semibold text-gray-900">API Reference</h2>
          </div>
          
          <div className="space-y-6">
            <div className="overflow-hidden border border-gray-200 rounded-lg">
              <div className="bg-gray-50 px-4 py-3 border-b border-gray-200">
                <div className="flex items-center">
                  <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                    POST
                  </span>
                  <code className="ml-2 text-sm font-mono text-gray-800">/api/chat</code>
                </div>
              </div>
              <div className="p-4 bg-white">
                <p className="text-sm text-gray-600 mb-3">Process a chat message and get a response.</p>
                <pre className="bg-gray-50 p-3 rounded text-xs overflow-x-auto">
                  {`{
  "message": "Your question here",
  "session_id": "optional-session-id"
}`}
                </pre>
              </div>
            </div>
            
            <div className="overflow-hidden border border-gray-200 rounded-lg">
              <div className="bg-gray-50 px-4 py-3 border-b border-gray-200">
                <div className="flex items-center">
                  <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">
                    GET
                  </span>
                  <code className="ml-2 text-sm font-mono text-gray-800">/api/articles</code>
                </div>
              </div>
              <div className="p-4 bg-white">
                <p className="text-sm text-gray-600">Retrieve a list of all articles in the knowledge base.</p>
              </div>
            </div>
          </div>
        </section>
      </div>
      
     
      
      <div className="bg-white rounded-lg shadow-md p-6 mb-8">
        <div className="flex items-center mb-6">
          <BookOpen className="w-6 h-6 text-blue-600 mr-2" />
          <span style={{ whiteSpace: 'pre' }}>   </span>
          <h2 className="text-2xl font-semibold">About This Project</h2>
        </div>
        
        <div className="prose max-w-none">
          <h3>Concept</h3>
          <p>
            This is a RAG (Retrieval-Augmented Generation) chatbot that combines the power of
            large language models with external knowledge retrieval. It can answer questions
            based on a collection of 50 articles in its knowledge base.
          </p>
          
          <h3 className="mt-6">Features</h3>
          <ul className="list-disc pl-5 space-y-2 mt-2">
            <li>Interactive chat interface for asking questions</li>
            <li>Knowledge base of 50 curated articles</li>
            <li>Documentation and usage guides</li>
            <li>Responsive design for all devices</li>
          </ul>
          
          <h3 className="mt-6">How It Works</h3>
          <ol className="list-decimal pl-5 space-y-2 mt-2">
            <li>User submits a question through the chat interface</li>
            <li>The system retrieves relevant information from the knowledge base</li>
            <li>The language model generates a response based on the retrieved information</li>
            <li>The response is displayed to the user</li>
          </ol>
        </div>
      </div>
      
      <div className="bg-white rounded-lg shadow-md p-6">
        <div className="flex items-center mb-6">
          <Code className="w-6 h-6 text-blue-600 mr-2" />
          <span style={{ whiteSpace: 'pre' }}>   </span>
          <h2 className="text-2xl font-semibold">Technical Details</h2>
        </div>
        
        <div className="prose max-w-none">
          <h3>Tech Stack</h3>
          <ul className="list-disc pl-5 space-y-1">
            <li>Frontend: React, React Router, Tailwind CSS</li>
            <li>Backend: Python, FastAPI</li>
            <li>Vector Database: FAISS (for efficient similarity search)</li>
            <li>Language Model: OpenAI's GPT (or your chosen model)</li>
          </ul>
          
          <h3 className="mt-6">API Endpoints</h3>
          <div className="bg-gray-50 p-4 rounded-md mt-2">
            <code className="text-sm">
              POST /api/chat - Submit a chat message<br />
              GET /api/articles - Get list of all articles<br />
              GET /api/articles/{"{id}"} - Get specific article details
            </code>
          </div>
        </div>
      </div>
    </div>
  );
}