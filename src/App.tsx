import { useState } from 'react'
import EmptyState from '@/components/EmptyState'
import SectionFrame from '@/components/SectionFrame'
import { sections } from '@/sections/registry'

export default function App() {
  const [activeSectionId, setActiveSectionId] = useState(sections[0]?.id ?? '')

  if (sections.length === 0) {
    return <EmptyState />
  }

  const activeSection =
    sections.find((section) => section.id === activeSectionId) ?? sections[0]

  return (
    <div className="flex h-screen flex-col overflow-hidden">
      {sections.length > 1 && (
        <nav className="flex shrink-0 items-center gap-2 border-b border-black/10 bg-white px-4 py-2">
          {sections.map((section) => {
            const isActive = section.id === activeSection.id

            return (
              <button
                key={section.id}
                type="button"
                onClick={() => setActiveSectionId(section.id)}
                className={`rounded-full px-4 py-2 text-sm font-medium transition-colors ${
                  isActive
                    ? 'bg-brand-500 text-white'
                    : 'bg-[#f7f4f1] text-[#1f1f1f] hover:bg-[#efeae4]'
                }`}
              >
                {section.label}
              </button>
            )
          })}
        </nav>
      )}

      <div className="min-h-0 flex-1">
        <SectionFrame title={activeSection.label} htmlPath={activeSection.htmlPath} />
      </div>
    </div>
  )
}
