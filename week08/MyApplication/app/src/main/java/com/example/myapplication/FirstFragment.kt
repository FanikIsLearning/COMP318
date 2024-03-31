package com.example.myapplication

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import com.example.myapplication.databinding.FragmentFirstBinding


/**
 * A simple [Fragment] subclass as the default destination in the navigation.
 */
class FirstFragment : Fragment() {

    private var _binding: FragmentFirstBinding? = null

    // This property is only valid between onCreateView and onDestroyView.
    private val binding get() = _binding!!

    private fun countMe() {
        // Get the current count or default to 0 if null or not a number
        val currentCount = binding.textviewFirst.text.toString().toIntOrNull() ?: 0
        // Increment the count
        val newCount = currentCount + 1
        // Set the new count to textview_first
        binding.textviewFirst.text = newCount.toString()
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        _binding = FragmentFirstBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        binding.randomButton.setOnClickListener {
            // Using binding to get the current text from textview_first
            val currentCount = binding.textviewFirst.text.toString().toIntOrNull() ?: 0
            // Creating an action with the current count to navigate to SecondFragment
            val action = FirstFragmentDirections.actionFirstFragmentToSecondFragment(currentCount)
            findNavController().navigate(action)
        }

        binding.toastButton.setOnClickListener {
            // create a Toast with some text, to appear for a short time
            val myToast = Toast.makeText(requireContext(), "Hello Toast!", Toast.LENGTH_SHORT)
            // show the Toast
            myToast.show()
        }

        binding.countButton.setOnClickListener {
            countMe()
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
