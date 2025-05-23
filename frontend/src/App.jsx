import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import ChatPage from './pages/chatPage';
import ArticlesPage from './pages/ArticlesPage';
import DocumentationPage from './pages/DocumentationPage';
import { CopyMinus  } from 'lucide-react';

function App() {
  return (
    <Router>
      <div className="relative flex size-full min-h-screen flex-col bg-white group/design-root overflow-x-hidden" style={{ fontFamily: 'Inter, "Noto Sans", sans-serif' }}>
        <div className="layout-container flex h-full grow flex-col">
          <header className="flex items-center justify-between whitespace-nowrap border-b  border-b-[#f0f2f5] px-10 py-3">
            <div className="flex items-center gap-4 text-[#111418]">
                <CopyMinus  />
              <span style={{ whiteSpace: 'pre' }}>   </span>
              <h2 className="text-[#111418] text-lg font-bold leading-tight tracking-[-0.015em]">  ragchatbot</h2>
            </div>
            <div className="flex flex-1 justify-end gap-8">
              <div className="flex items-center gap-9">
                <Link to="/articles" className="no-underline text-[#111418] text-sm font-medium leading-normal hover:text-[#0c7ff2]">
                  Articles
                </Link>
                <span style={{ whiteSpace: 'pre' }}>    </span>
                <Link to="/documentation" className="no-underline text-[#111418] text-sm font-medium leading-normal hover:text-[#0c7ff2]">
                  Documentation
                </Link>
              </div>
            </div>
          </header>
          
          <main className="flex-1">
            <Routes>
              <Route path="/" element={<ChatPage />} />
              <Route path="/articles" element={<ArticlesPage />} />
              <Route path="/documentation" element={<DocumentationPage />} />
            </Routes>
          </main>
        </div>
      </div>
    </Router>
  );
}

export default App;