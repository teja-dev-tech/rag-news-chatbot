import { useState, useRef, useEffect } from 'react';
import { useChatApi } from '../hooks/useChatApi';

export default function ChatPage() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const messagesEndRef = useRef(null);
  const { sendMessage, isLoading, error } = useChatApi();

  // Auto-scroll to bottom when messages change
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { id: Date.now(), role: 'user', content: input };
    setMessages(prev => [...prev, userMessage]);
    
    const userInput = input;
    setInput('');

    try {
      const response = await sendMessage(userInput);
      
      setMessages(prev => [
        ...prev,
        { id: Date.now() + 1, role: 'assistant', content: response }
      ]);
    } catch (err) {
      console.error('Error sending message:', err);
      setMessages(prev => [
        ...prev,
        { 
          id: Date.now() + 1, 
          role: 'assistant', 
          content: 'Sorry, I encountered an error. Please try again.' 
        }
      ]);
    }
  };

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  return (
    <div className="px-40 flex flex-1 justify-center py-5">
      <div className="layout-content-container flex flex-col max-w-[960px] flex-1">
        <h2 className="text-[#111418] tracking-light text-[28px] font-bold leading-tight px-4 text-center pb-3 pt-5">
          RAG News Chatbot
        </h2>
        
        {/* Messages container */}
        <div className="flex-1 overflow-y-auto mb-4 px-4">
          {messages.length === 0 ? (
            <div className="flex items-center justify-center h-full text-gray-500">
              Welcome to the RAG News Chatbot!
            </div>
          ) : (
            <div className="space-y-4">
              {messages.map((message) => (
                <div
                  key={message.id}
                  className={`flex ${message.role === 'user' ? 'justify-end' : 'justify-start'}`}
                >
                  <div
                    className={`max-w-[80%] rounded-lg p-4 ${
                      message.role === 'user'
                        ? 'bg-[#0c7ff2] text-white rounded-br-none'
                        : 'bg-[#f0f2f5] text-[#111418] rounded-bl-none'
                    }`}
                  >
                    {message.content}
                  </div>
                </div>
              ))}
              <div ref={messagesEndRef} />
            </div>
          )}
        </div>

       {/* Input area */}
        <div className="px-4 py-3">
          <form onSubmit={handleSubmit} className="flex items-center gap-2">
            <input
              type="text"
              placeholder="Ask me anything about the latest news"
              className="flex-1 bg-[#f0f2f5] text-[#111418] placeholder-[#60758a] px-4 py-2 rounded-lg text-base border border-gray-300"
              value={input}
              onChange={handleInputChange}
              disabled={isLoading}
            />
            <button
              type="submit"
              disabled={!input.trim() || isLoading}
              className={`px-4 py-2 rounded-lg text-sm font-medium ${
                input.trim() && !isLoading
                  ? 'bg-[#0c7ff2] text-white hover:bg-[#0a6bd9]'
                  : 'bg-gray-200 text-gray-400 cursor-not-allowed'
              }`}
            >
              {isLoading ? 'Sending...' : 'Send'}
            </button>
          </form>

          {error && (
            <div className="mt-2 text-red-500 text-sm text-center">
              Error: {error}
            </div>
          )}
        </div>

      </div>
    </div>
  );
}
